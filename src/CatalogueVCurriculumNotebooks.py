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

'''
Client ID
44425752492-sr2cun8r7jn2s3n1f14ue760hgi5jv9u.apps.googleusercontent.com
'''

'''
Client Secret
vsIHUqonxrViuiOMzg4IbRUw
'''

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
CurriculumWebsite_SPREADSHEET_ID = '1pw-p7uluSa7xWwHYn7ZgQ8jxkHwXnkDJa_NLR44TbS8'
Website_RANGE_NAME = 'Sheet1!A1:F38'
CurriculumCatalogue_SPREADSHEET_ID = '1ZJ1jux31RFV_dgiBLS4DWLlKSPvjFQAjvvHj5y0hwfE'
Catalogue_RANGE_NAME = 'Catalogue!A1:I121'
JSON_CREDENTIALS = 'client_secret_44425752492-sr2cun8r7jn2s3n1f14ue760hgi5jv9u.apps.googleusercontent.com.json' 

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
    values_website[0][5]: [values_website[i][5] for i in range(1, number_iterations)]}
    
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
        
    values_catalogue = get_sheet(CurriculumCatalogue_SPREADSHEET_ID,Catalogue_RANGE_NAME,JSON_CREDENTIALS)