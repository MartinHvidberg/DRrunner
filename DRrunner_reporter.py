# Running Data Reviewer, via ArcPy
# This .py file is the Reporting module
# It's supposed to be called from either the Commendline- or 
# the ArcMapGUI-module'
# You Very likely want to run the DRrunner_execute.py before this module.

import arcpy

def make_report_of_errors(DR_db, run_nr):
    print "    make_report_of_errors() : "+str(DR_db) + " / " + str(run_nr)
    # SearchCursor (in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})
    fc = DR_db+"\REVCHECKRUNTABLE"
    fields = ["BATCHRUNID", "SESSIONID", "CHECKRUNID", "BATCHJOBNAME", "BATCHJOBDATETIME", "BATCHJOBGROUPNAME", "CHECKNAME", "CHECKTITLE", "RESOURCENAME", "PARAMETERS", "TOTALVALIDATED", "TOTALRESULTS"]
    expression = arcpy.AddFieldDelimiters(fc, "BATCHRUNID") + " = '" + str(run_nr.strip("{}"))+"'" # <--- Never really worked with them bloody GUIDs
    with arcpy.da.SearchCursor(fc, fields) as cursor:
        for row in cursor:
            str_this_batchrunid = row[0] # Because "BATCHRUNID" is first in fields ...
            if str_this_batchrunid == run_nr:
                print "    ====== REVRUNCHECKTABLE ============="
                for i in range(len(fields)):
                    print "    "+fields[i] + " : " + str(row[i])
            else:
                print "    No match:"
                print "        " + str_this_batchrunid
                print "        " + run_nr
        dic_return = dict()
    
    return

def show_report(report):
    print " XXX I show one report ..."
    return

def email_reports(lst_reports):
    print " XXX I email the reports ..."
    return