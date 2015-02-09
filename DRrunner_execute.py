# Running Data Reviewer, via ArcPy
# This .py file is the Executing module
# It's supposed to be called from either the Commendline- or 
# the ArcMapGUI-module'

import arcpy
    
# Check out a Data Reviewer extension license
arcpy.CheckOutExtension("datareviewer")

def DRrun(str_dr_db, str_filename_rbj, str_data_db):
    print "inside DRrun ..."
    
    # Description: Executes a reviewer batch job
    # Requirements: Production Mapping extension
    
    arcpy.env.overwriteOutput="true"
    
    # Delete, and then Create, the DR-session, to make sure it's clean.
    print "Starting DR session"
    str_session = "Session 1 : DRrunner"
    try:
        arcpy.DeleteReviewerSession_Reviewer(str_dr_db, str_session)
    except:
        print "   Session didn't exist - now creating it ..."
    arcpy.CreateReviewerSession_Reviewer(str_dr_db, str_session)
    print "   DR session Create - Success"
    
    # Execute Reviewer Batch Job function
    print "Executing DR batch job: "+str_filename_rbj
    res = arcpy.ExecuteReviewerBatchJob_Reviewer(str_dr_db, str_session, str_filename_rbj, str_data_db)
    print "   DR execute rbj - Success"
    
    # get the output table
    tbl = res.getOutput(0)
    print tbl.name
    
    # query the table
    for row in arcpy.da.SearchCursor(tbl,("RECORDID","BATCHJOBID","BATCHJOBFILE")):
        print str(row[0])
        print row[1]
        print row[2]
    
    # Check in the Data Reviewer extension
    arcpy.CheckInExtension("datareviewer")

    # ------ End def DRrun() -------------

# Music that accompanied the coding of this script:
#   Coralie Clement - Salle des pas perdus