import EmployeeShiftInformationClass
import sys
import json

scheduleJSON = sys.argv[1]
employeeidJSON = sys.argv[2]
schedule=json.loads(scheduleJSON)
employeeid=json.loads(employeeidJSON)

class ManagerCreateEmployeePreferenceController:
    def ManagerCreateEmployeePreferenceController(schedule, employeeid):
        mcepc = EmployeeShiftInformationClass.EmployeeShiftInformation()
        mcepc.ManagerCreateEmployeeShiftPreferece(schedule,employeeid)

mcepc = ManagerCreateEmployeePreferenceController.ManagerCreateEmployeePreferenceController(schedule, employeeid)