# Running Data Reviewer, via ArcPy
# This .py file is the Reporting module
# It's supposed to be called from either the Commendline- or 
# the ArcMapGUI-module'
# You Very likely want to run the DRrunner_execute.py before this module.

import arcpy

def make_report_of_errors(DR_db, run_nr):
    print " > DRrunner_reporter.make_report_of_errors() : "+str(DR_db) + " / " + str(run_nr)
    dic_return = dict()
    # SearchCursor (in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})
    fc_rcrt = DR_db+"\REVCHECKRUNTABLE"
    fields_rcrt = ["BATCHRUNID", "SESSIONID", "BATCHJOBNAME", "BATCHJOBDATETIME", "BATCHJOBGROUPNAME", "CHECKNAME", "CHECKTITLE", "RESOURCENAME", "TOTALVALIDATED", "TOTALRESULTS"] # "CHECKRUNID", "PARAMETERS", 
    expression = arcpy.AddFieldDelimiters(fc_rcrt, "BATCHRUNID") + " = '" + str(run_nr.strip("{}"))+"'" # <--- Never really worked with them bloody GUIDs
    with arcpy.da.SearchCursor(fc_rcrt, fields_rcrt) as cursor_rcrt:
        for row_rcrt in cursor_rcrt:
            str_this_batchrunid = row_rcrt[0] # Because "BATCHRUNID" is first in fields_rcrt ...
            if str_this_batchrunid == run_nr:
                print "    ====== REVRUNCHECKTABLE ============="
                for i in range(len(fields_rcrt)):
                    print "    "+fields_rcrt[i] + " : " + str(row_rcrt[i])
                    dic_return[fields_rcrt[i]] = str(row_rcrt[i])
                #-----------------------------
                if int(dic_return["TOTALRESULTS"]) > 0:
                    dic_return["Error"] = list()
                    fc_rtm = DR_db+"\REVTABLEMAIN"
                    fields_rtm = ["SESSIONID", "OBJECTID", "ORIGINTABLE", "REVIEWSTATUS"]
                    with arcpy.da.SearchCursor(fc_rtm, fields_rtm) as cursor_rtm:
                        for row_rtm in cursor_rtm:
                            dic_error = dict()
                            num_this_sessionid = int(row_rtm[0]) # Because "SESSIONID" is first in fields_rtm ...
                            num_wanted_sessionid = int(dic_return["SESSIONID"])
                            if num_this_sessionid == num_wanted_sessionid:
                                print "    >    ------ REVTABLEMAIN --------------"
                                for j in range(len(fields_rtm)):
                                    if j>0: # Don't save SESSIONID again
                                        #print "    >    "+fields_rtm[j] + " : " + str(row_rtm[j])
                                        dic_error[fields_rtm[j]] = str(row_rtm[j])
                                print "    dic_error:", dic_error
                                lst_errors = dic_return["Error"]
                                lst_errors.append(dic_error)
                                dic_return["Error"] = lst_errors   
                            #else:
                            #    print "No hit: ", str(type(num_this_sessionid)),num_this_sessionid, str(type(dic_return["SESSIONID"])),dic_return["SESSIONID"]
                #-----------------------------
                #print str(dic_return)
            #else:
            #    print "    No match:"
            #    print "        " + str_this_batchrunid
            #    print "        " + run_nr
    print " < DRrunner_reporter.make_report_of_errors() Done ... : "+str(DR_db) + " / " + str(run_nr)
    return dic_return

def show_report(report):
    print " XXX I show one report ..."
    return

def email_reports(lst_reports):
    print " XXX I email the reports ..."
    return