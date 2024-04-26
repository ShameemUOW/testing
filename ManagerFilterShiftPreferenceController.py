import EmployeeShiftInformationClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
day = x["day"]
shiftpref = x["shiftpref"]

class ManagerFilterShiftPreferenceController:
    def managerfilterpreference(day,shiftpref):
        mfilterpref = EmployeeShiftInformationClass.EmployeeShiftInformation()
        mfilterpref.FilterShiftPreference(day,shiftpref)

mfp = ManagerFilterShiftPreferenceController.managerfilterpreference(day,shiftpref)