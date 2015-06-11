# Data Reviewer Data Base - objects

class DRDB_rbj_result(object):
    """ DRDB - A rbj Result. 
    The output parameter for arcpy.ExecuteReviewerBatchJob_Reviewer()
    is a table view of one row of the REVBATCHRUNTABLE table in the Reviewer Workspace. 
    The row represents the record created when the batch job is executed.
    """
    
    def __init__(self, dr_ws="", run_id="{00000000-0000-0000-0000-000000000000}"):
        """ DRDB_session_result.__init__() """
        self.run_id = run_id
    