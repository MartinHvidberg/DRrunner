# Running Data Reviewer, via ArcPy
# This .py file is the Command line version.
# It's very short, it simply calls the main executing module,
# after setting up a few parameters.

import DRrunner_execute

if __name__ == "__main__":
    
    # Set reviewer workspace
    reviewer_db = r"C:\Martin\Work\DR.gdb"
    
    # reviewer batch job file
    str_filename_rbj = r"C:\Martin\Work\DRrun_test.rbj"
    
    # production database - contains data to validate
    str_data_db = "C:\Martin\NIScopy140830.gdb" # "C:/gisdata/Edit_Sample.sde"
    
    DRrunner_execute.DRrun(reviewer_db, str_filename_rbj, str_data_db)

# Music that accompanied the coding of this script:
#   