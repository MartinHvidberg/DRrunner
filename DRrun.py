# Running Data Reviewer, via ArcPy
# This .py file is the Command line version.
# It's very short, it simply calls the main executing module,
# after setting up a few parameters.

import sys
import os.path
# import ECtimer XXX
import DRrunner_execute
import DRrunner_reporter

if __name__ == "__main__":
    
    # *** Init
    
    print "DRrun : Init phase Begin ..."    
    # *Setup parameters
    arcpy.env.overwriteOutput="true"    
    # Set reviewer workspace
    reviewer_db = r"C:\Martin\Work\DR_runner_10_3_GR96.gdb"    
    # reviewer batch job file
    lst_filename_rbj = [r"C:\Martin\Work\DRrunner_check1.rbj",r"C:\Martin\Work\DRrunner_check2.rbj"]    
    # production database - contains data to validate
    str_data_db = "C:\Martin\Work\NIScopy.gdb" # "C:/gisdata/Edit_Sample.sde"      
    # Check existance and validity of the above parameters
    if not os.path.exists(reviewer_db):
        print "!!! Can't find reviewer_db: "+reviewer_db
        sys.exit(101)
    for str_filename_rbj in lst_filename_rbj:
        if not os.path.exists(str_filename_rbj):
            print "!!! Can't find filename_rbj: "+str_filename_rbj
            sys.exit(102)
    if not os.path.exists(str_data_db):
        print "!!! Can't find data_db: "+str_data_db
        sys.exit(103)
    print "DRrun : Init phase End ..." 
        
    # *** Run the checks
     
    print "DRrun : Running phase Begin ..."        
    lst_run_ids = list() # to cache the returning run IDs
    for str_filename_rbj in lst_filename_rbj:
        print "DRrun : call executer"
        lst_run_ids.append(DRrunner_execute.DRrun(reviewer_db, str_filename_rbj, str_data_db))
        print "DRrun : returned from executer"
    print "DRrun : Returned the following ids:"
    for run_id in lst_run_ids:
        print "DRrun :    runID: "+str(run_id)        
    print "DRrun : Running phase End ..."
    
    # *** Optionally display the errors found ...
    
    print "DRrun : Reporting phase Begin ..."         
    lst_error_reports = list()
    for id_i in lst_run_ids:
        dic_error_report = DRrunner_reporter.make_report_of_errors(reviewer_db, id_i)
        print "\n* This is the raw report:\n"+str(dic_error_report)
        DRrunner_reporter.show_report(dic_error_report)
    DRrunner_reporter.email_reports(lst_error_reports)    
    print "DRrun : Reporting phase End ..."

# Music that accompanied the coding of this script:
#    Doors - L.A.Woman
#   