import EmployeeShiftInformationClass
import sys
import json

scheduleJSON = sys.argv[1]
employeeidJSON = sys.argv[2]
schedule=json.loads(scheduleJSON)
employeeid_load=json.loads(employeeidJSON)
employeeid = employeeid_load["employeeid"]

class EmployeeUpdateShiftPreferenceController:
    def EmployeeUpdateShiftPreferenceController(schedule, employeeid):
        mcepc = EmployeeShiftInformationClass.EmployeeShiftInformation()
        mcepc.EmployeeUpdateShiftPreference(schedule,employeeid)

mcepc = EmployeeUpdateShiftPreferenceController.EmployeeUpdateShiftPreferenceController(schedule, employeeid)