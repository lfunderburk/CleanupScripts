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
