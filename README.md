# CleanupScripts
Repository containing scripts to cleanup Callysto Curriculum and Catalogue Information

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

Working example to spreadsheet [Curriculum notebooks table for website](https://docs.google.com/spreadsheets/d/1pw-p7uluSa7xWwHYn7ZgQ8jxkHwXnkDJa_NLR44TbS8/edit#gid=0)
        %python3 CatalogueVCurriculumNotebooks.py '1pw-p7uluSa7xWwHYn7ZgQ8jxkHwXnkDJa_NLR44TbS8' 'Sheet1!A1:G82' '1ZJ1jux31RFV_dgiBLS4DWLlKSPvjFQAjvvHj5y0hwfE' 'Catalogue!A1:I121' '/Users/laura.gf/Documents/Callysto/curriculum-notebooks/'
