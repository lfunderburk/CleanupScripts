# Author: Laura Gutierrez Funderburk
# Created on December 16 2019
# Last modified on December 23 2019
'''
Description: This script performs cross comparison of notebooks in the 'Curriculum notebooks table for website'
(URL https://docs.google.com/spreadsheets/d/1pw-p7uluSa7xWwHYn7ZgQ8jxkHwXnkDJa_NLR44TbS8/edit?usp=sharing) 
against notebooks found in GitHub repository https://github.com/callysto/curriculum-notebooks
and determines what notebooks are in the repository that have not been added to spreadsheet. 

Similarly, this script then compares 'Curriculum notebooks table for website'
(URL https://docs.google.com/spreadsheets/d/1pw-p7uluSa7xWwHYn7ZgQ8jxkHwXnkDJa_NLR44TbS8/edit?usp=sharing)  
against 'Callysto Notebook Development Catalogue' (URL https://docs.google.com/spreadsheets/d/1ZJ1jux31RFV_dgiBLS4DWLlKSPvjFQAjvvHj5y0hwfE/edit?usp=sharing)
and determines what notebooks are missing in the  'Curriculum notebooks table for website' table
'''
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import re
import pandas as pd 
import os

'''
Client ID
44425752492-sr2cun8r7jn2s3n1f14ue760hgi5jv9u.apps.googleusercontent.com
'''

'''
Client Secret
vsIHUqonxrViuiOMzg4IbRUw
'''

def get_sheet(spreadsheet_ID,range_name,JSON_credentials):
    """Takes as input a spreadsheet ID, range, and JSON file with credentials.
    Return values from associated spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                JSON_credentials, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_ID,
                                range=range_name).execute()
    values = result.get('values', [])

    return values

if __name__ == '__main__':
    
    # variable area
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # The ID and range of a sample spreadsheet.
    CurriculumWebsite_SPREADSHEET_ID = '1pw-p7uluSa7xWwHYn7ZgQ8jxkHwXnkDJa_NLR44TbS8'
    Website_RANGE_NAME = 'Sheet1!A1:G82'
    CurriculumCatalogue_SPREADSHEET_ID = '1ZJ1jux31RFV_dgiBLS4DWLlKSPvjFQAjvvHj5y0hwfE'
    Catalogue_RANGE_NAME = 'Catalogue!A1:I121'
    JSON_CREDENTIALS = 'client_secret_44425752492-sr2cun8r7jn2s3n1f14ue760hgi5jv9u.apps.googleusercontent.com.json' 
    path_to_cloned_repository = '/Users/laura.gf/Documents/Callysto/curriculum-notebooks/'
    
    ####################################################################################################################
    # Google Sheet Curriculum Data (website) 
    # Parse Website sheet
    values_website = get_sheet(CurriculumWebsite_SPREADSHEET_ID,Website_RANGE_NAME,JSON_CREDENTIALS)
    
    # Get number of rows in spreadsheet
    number_iterations = len(values_website)
    
    # Build dictonary with column names and values
    df_dictionary = {
    values_website[0][0]: [values_website[i][0] for i in range(1, number_iterations)],
    values_website[0][1]: [values_website[i][1] for i in range(1, number_iterations)],
    values_website[0][2]: [values_website[i][2] for i in range(1, number_iterations)],
    values_website[0][3]: [values_website[i][3] for i in range(1, number_iterations)],
    values_website[0][4]: [values_website[i][4] for i in range(1, number_iterations)],
    values_website[0][5]: [values_website[i][5] for i in range(1, number_iterations)],
    values_website[0][6]: [values_website[i][6] for i in range(1, number_iterations)]}
    
    # Construct Dataframe from dictionary
    CC_data = pd.DataFrame.from_dict(df_dictionary)

    # Get link list 
    link_list = CC_data["Link"].tolist()
    
    # Iterate over all links and use the .search method to get path to notebook (minus notebook name)
    all_links = []
    for i in range(len(link_list)):
        match = re.search(".*/", link_list[i])
        all_links.append(match.group())
    
    # Create new field with path to notebook
    CC_data["CrossCompLink"] = all_links
    
    ####################################################################################################################
    # REPOSITORY DATA 
    # Iterate over each directory in the cloned repository 
    count = 0
    root_s = []
    file_s = []
    for root, dirs, files in os.walk(path_to_cloned_repository):
        # If a notebook is found in any of the files 
        if any(".ipynb" in x for x in files):
            # Get path
            root_s.append(root)
            # Get file names 
            file_s.append(files)
            
    # Create dataframe from repository data
    LC_data = pd.DataFrame.from_dict({"Path":root_s,"Files":file_s})
    
    # Cleanup
    LC_data = LC_data.replace(path_to_cloned_repository,"",regex=True)
    LC_data[['Subject','Topic']] = LC_data["Path"].str.split("/",n=1,expand=True)
    # Subject to change below
    LC_data["Subject"] = LC_data["Subject"].replace("Mathematics",'Math',regex=True)
    LC_data["Subject"] = LC_data["Subject"].replace("Technology","Computer Science",regex=True)
    
    # Create links to peform cross comparison
    LC_data["Link"] = "https://github.com/callysto/curriculum-notebooks/blob/master/" + LC_data["Path"] + "/"
    
    # Compare links in both
    Link_intersection = set(LC_data["Link"]).intersection(set(CC_data["CrossCompLink"]))
    # Determine what links are in the repository which are missing in the google spreadsheet
    Missing_links = list(set(LC_data["Link"]).difference(Link_intersection))
    
    # Iterate over each of the rows whose link is reported as a'missing link' 
    
    # Column names (for reference) ['Subject', 'Grade', 'Title', 'Description', 'Link', 'GitPuller Link', 'CrossCompLink']
    for i in range(1,len(Missing_links)):
        # Get ith row with a missing link
        vals = LC_data[LC_data["Link"]==Missing_links[i]].values[0]

        
        for item in vals[1]:
            if ".ipynb" in item:
                # Cleanup name 
                file_nam = item
                final_name = re.sub(r"(\w)([A-Z])", r"\1 \2", file_nam.split(".")[0])
                final_name = re.sub("-", " ", final_name)
                final_name = re.sub("_", " ", final_name)

                CC_data.loc[36+i] = [vals[2],\
                                       "", final_name,\
                                    "",vals[4] + file_nam,"",""]  # adding a row

            else:
                continue
    CC_data.to_excel("Curriculum_notebooks_table_or_websit_2019_12_24.xlsx")

    values_catalogue = get_sheet(CurriculumCatalogue_SPREADSHEET_ID,Catalogue_RANGE_NAME,JSON_CREDENTIALS)
