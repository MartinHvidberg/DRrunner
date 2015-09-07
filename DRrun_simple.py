import arcpy
arcpy.checkOutExtension("datareviewer")
arcpy.ImportToolbox("C:/Program Files (x86)/ArcGIS/ArcGISDataReviewer/Desktop10.3/ArcToolbox/Toolboxes/Data Reviewer Tools.tbx")
arcpy.ExecuteBatchJob_Reviewer(Data_Reviewer_Workspace, Session_Name, Batch_job, "", "")
arcpy.checkInExtension("datareviewer")
