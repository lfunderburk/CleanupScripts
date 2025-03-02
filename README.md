# CleanupScripts

Repository containing scripts to cleanup Callysto Curriculum and Catalogue Information.

## Script Description

Description: This script performs cross comparison of notebooks in the 'Curriculum notebooks table for website'
(URL https://docs.google.com/spreadsheets/d/1pw-p7uluSa7xWwHYn7ZgQ8jxkHwXnkDJa_NLR44TbS8/edit?usp=sharing) 
against notebooks found in GitHub repository https://github.com/callysto/curriculum-notebooks
and determines what notebooks are in the repository that have not been added to spreadsheet. 

Similarly, this script then compares 'Curriculum notebooks table for website'
(URL https://docs.google.com/spreadsheets/d/1pw-p7uluSa7xWwHYn7ZgQ8jxkHwXnkDJa_NLR44TbS8/edit?usp=sharing)  
against 'Callysto Notebook Development Catalogue' (URL https://docs.google.com/spreadsheets/d/1ZJ1jux31RFV_dgiBLS4DWLlKSPvjFQAjvvHj5y0hwfE/edit?usp=sharing)
and determines what notebooks are missing in the  'Curriculum notebooks table for website' table

## Script Usage

    usage python3 CatalogueVCurriculumNotebooks.py -h 


      usage: CatalogueVCurriculumNotebooks.py [-h]
                                              website_spreadsheet_id
                                              website_spreadsheet_range
                                              catalogue_spreadsheet_id
                                              catalogue_spreadsheet_range
                                              github_rep_path

      Cross comparison of content between GitHub repostory and Listed Notebooks in Callysto Curriculum Website.

      positional arguments:
        website_spreadsheet_id
                                    Google Spreadsheet ID associated to Curriculum Website ID.
        website_spreadsheet_range
                                    Range of coverage specified by sheet name and range, i.e. 'Sheet1!A1:G82'
        catalogue_spreadsheet_id
                                    Google Spreadsheet ID associated to Curriculum Catalogue ID.
        catalogue_spreadsheet_range
                                    Range of coverage specified by sheet name and range, i.e. 'Sheet1!A1:G82'
        github_rep_path             Full path to cloned GitHub repository https://github.com/callysto/curriculum-notebooks

      optional arguments:
        -h, --help            show this help message and exit

Working example to spreadsheet [Curriculum notebooks table for website](https://docs.google.com/spreadsheets/d/1pw-p7uluSa7xWwHYn7ZgQ8jxkHwXnkDJa_NLR44TbS8/edit#gid=0) where its ID is 

    1pw-p7uluSa7xWwHYn7ZgQ8jxkHwXnkDJa_NLR44TbS8
    
and range Sheet1!A1:G82. 

Similarly, [Callysto Notebook Development Catalogue
](https://docs.google.com/spreadsheets/d/1ZJ1jux31RFV_dgiBLS4DWLlKSPvjFQAjvvHj5y0hwfE/edit#gid=0) whose spreadsheet ID is       
            
            1ZJ1jux31RFV_dgiBLS4DWLlKSPvjFQAjvvHj5y0hwfE 
            
and range Catalogue!A1:I121. 

For this example, we git cloned the repository [Callysto Curriculum Notebooks](https://github.com/callysto/curriculum-notebooks) in local directory 

        /Users/laura.gf/Documents/Callysto/curriculum-notebooks/


Begin working example 

        %python3 CatalogueVCurriculumNotebooks.py '1pw-p7uluSa7xWwHYn7ZgQ8jxkHwXnkDJa_NLR44TbS8' 'Sheet1!A1:G82' '1ZJ1jux31RFV_dgiBLS4DWLlKSPvjFQAjvvHj5y0hwfE' 'Catalogue!A1:I121' '/Users/laura.gf/Documents/Callysto/curriculum-notebooks/'
