# Running Data Reviewer, via ArcPy
# This .py file is the Executing module
# It's supposed to be called from either the Commendline- or 
# the ArcMapGUI-module'

import arcpy
    
# Check out a Data Reviewer extension license
arcpy.CheckOutExtension("datareviewer")

def DRrun(str_dr_db, str_filename_rbj, str_data_db):
    print "DRexe : DRrunner_execute()", str_dr_db, str_filename_rbj, str_data_db
    
    # Description: Executes a reviewer batch job
    # Requirements: Production Mapping extension
    
    arcpy.env.overwriteOutput="true"
    
    # Delete, and then Create, the DR-session, to make sure it's clean.
    print "DRexe : Starting DR session"
    str_jobName = str_filename_rbj[:-4]
    if str_jobName.rfind("\\")>0:
        str_jobName = str_jobName[str_jobName.rfind("\\")+1:]    
    str_session = "DRrun_"+str_jobName # A simple string won't cut it, I need to collect the full names ... XXX
    try:
        arcpy.DeleteReviewerSession_Reviewer(str_dr_db, str_session)
        # XXX Consider to delete all sessions older than e.g. 1 month.

    except:
        pass # print "DRexe : Session didn't exist - deleting nothing ..."
    drs_session = arcpy.CreateReviewerSession_Reviewer(str_dr_db, str_session)
    #Session = arcpy.CreateReviewerSession_Reviewer(Reviewer_workspace , "TestSession", "Session 1 : Session 1")
    print "DRexe : DR session Create - Success : ", str(drs_session)
    
    # Execute Reviewer Batch Job function
    print "DRexe : Executing DR batch job: "+str_filename_rbj
    res = arcpy.ExecuteReviewerBatchJob_Reviewer(str_dr_db, drs_session, str_filename_rbj, str_data_db)
    print "DRexe : DR execute rbj - Success"
    
    # get the output table
    print "DRexe : Show results 1 of "+str(len(res))+" (recordid, globalid, batchjobfile, runcontext, status, starttime, endtime) :"
    tbl = res.getOutput(0)
    # query the table
    for row in arcpy.da.SearchCursor(tbl,("*")):
        #for i in range(len(row)):
        #    print "DRexe :  > "+str(i)+" : "+str(row[i])
        print "DRexe :    "+str(row)
        str_batch_run_id = row[1]
    
    print "DRexe : DRrunner_execute() - Done... : ", str_batch_run_id
    return str_batch_run_id

    # ------ End def DRrun() -------------

# Music that accompanied the coding of this script:
#   Coralie Clement - Salle des pas perdus