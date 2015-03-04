# Running Data Reviewer, via ArcPy
# This .py file is the Command line version.
# It's very short, it simply calls the main executing module,
# after setting up a few parameters.

import sys
import os.path
import DRrunner_execute

if __name__ == "__main__":
    
    # *** Setup parameters
    
    # Set reviewer workspace
    reviewer_db = r"C:\Martin\Work\Data_Reviewer\DRrunner.gdb"    
    # reviewer batch job file
    str_filename_rbj = r"C:\Martin\Work\NamesA_DomainsCheck.rbj"    
    # production database - contains data to validate
    str_data_db = "C:\Martin\Work\mahvi_1135_Qaqortoq.gdb" # "C:/gisdata/Edit_Sample.sde"    
    # Check existance and validity of the above parameters
    if not os.path.exists(reviewer_db):
        print "Can't find reviewer_db: "+reviewer_db
        sys.exit(-1)
    if not os.path.exists(str_filename_rbj):
        print "Can't find str_filename_rbj: "+str_filename_rbj
        sys.exit(-2)
    if not os.path.exists(str_data_db):
        print "Can't find str_data_db: "+str_data_db
        sys.exit(-3)
        
    # *** Run the checks
    
    # Run
    lst_run_ids = list()
    lst_run_ids.append(DRrunner_execute.DRrun(reviewer_db, str_filename_rbj, str_data_db))
    print "Done running - returning following ids:"
    for run_id in lst_run_ids:
        print "    : "+str(run_id)
    
    # Optionally display the errors found ...
    

# Music that accompanied the coding of this script:
#   