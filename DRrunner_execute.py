# Running Data Reviewer, via ArcPy
# This .py file is the Executing module
# It's supposed to be called from either the Commendline- or 
# the ArcMapGUI-module'

import arcpy
    
# Check out a Data Reviewer extension license
arcpy.CheckOutExtension("datareviewer")

def DRrun(str_dr_db, str_filename_rbj, str_data_db):
    print " > DRrunner_execute()", str_dr_db, str_filename_rbj, str_data_db
    
    # Description: Executes a reviewer batch job
    # Requirements: Production Mapping extension
    
    arcpy.env.overwriteOutput="true"
    
    # Delete, and then Create, the DR-session, to make sure it's clean.
    print "Starting DR session"
    str_session = "DRrunner" # A simple string wont cut it, I need to collect the full names ... XXX
    try:
        arcpy.DeleteReviewerSession_Reviewer(str_dr_db, str_session)
        # XXX Consider to delete all sessions older than e.g. 1 month.
        # session="Session 1 : qc01"
        # arcpy.DeleteReviewerSession_Reviewer(reviewer_gdb,session)

    except:
        pass # print "   Session didn't exist - deleting nothing ..."
    drs_session = arcpy.CreateReviewerSession_Reviewer(str_dr_db, str_session)
    #Session = arcpy.CreateReviewerSession_Reviewer(Reviewer_workspace , "TestSession", "Session 1 : Session 1")
    print "   DR session Create - Success : ", str(drs_session)
    
    # Execute Reviewer Batch Job function
    print "Executing DR batch job: "+str_filename_rbj
    res = arcpy.ExecuteReviewerBatchJob_Reviewer(str_dr_db, drs_session, str_filename_rbj, str_data_db)
    print "   DR execute rbj - Success"
    
    # get the output table
    print "Show results 1 of "+str(len(res))+" (recordid, globalid, batchjobfile,runcontext, status, starttime, endtime) :"
    tbl = res.getOutput(0)
    # query the table
    for row in arcpy.da.SearchCursor(tbl,("*")):
        for i in range(len(row)):
            print "    "+str(i)+" : "+str(row[i])
        str_batch_run_id = row[1]
    
    # Check in the Data Reviewer extension
    arcpy.CheckInExtension("datareviewer")
    
    print " < DRrunner_execute() - Done... : ", str_batch_run_id
    return str_batch_run_id

    # ------ End def DRrun() -------------

# Music that accompanied the coding of this script:
#   Coralie Clement - Salle des pas perdus