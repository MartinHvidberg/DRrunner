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
    arcpy.env.overwriteOutput="true"    
    # Set reviewer workspace
    reviewer_db = r"C:\Martin\Work\DR_runner_10_3_GR96.gdb"   
    if not os.path.exists(reviewer_db):
        print "!!! Can't find reviewer_db: "+reviewer_db
        sys.exit(101) 
    # reviewer batch job file(s)
    if len(sys.argv) > 0:
        fil_ecbrbj = sys.argv[1]
        lst_filename_rbj = list()
        try:
            with open(fil_ecbrbj, 'r') as infile:        
                for line in infile:
                    if len(line.strip()) > 0 and line.strip()[0] != "#":
                        lst_filename_rbj.append(line.strip())
        except:
            print "DRrun : !!! Can't open the .ecbrbj file: "+fil_ecbrbj
            sys.exit(103)  
    else:
        print "DRrun : !!! No .ecbrbj file on the command line"
        sys.exit(102)
    lst_filenames_good = list()
    for str_filename_rbj in lst_filename_rbj:
        if os.path.exists(str_filename_rbj):
            lst_filenames_good.append(str_filename_rbj)
        else:
            print "DRrun : !!! While processing "+fil_ecbrbj+" : Can't find filename_rbj: "+str_filename_rbj
    lst_filename_rbj = lst_filenames_good
    # production database - contains data to validate
    str_data_db = "C:\Martin\Work\NIScopy.gdb" # "C:/gisdata/Edit_Sample.sde"   
    if not os.path.exists(str_data_db):
        print "!!! Can't find data_db: "+str_data_db
        sys.exit(104)   
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
        DRrunner_reporter.show_report(dic_error_report)
    DRrunner_reporter.email_reports(lst_error_reports)    
    print "DRrun : Reporting phase End ..."

# Music that accompanied the coding of this script:
#    Doors - L.A.Woman
#    C.V. Joergensen - Tidens tern
#   