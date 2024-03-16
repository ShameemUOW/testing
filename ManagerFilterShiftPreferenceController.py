import EmployeeShiftInformationClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
selectedoption = x["selectedoption"]

class ManagerFilterShiftPreferenceController:
    def managerfilterpreference(selectedoption):
        mfilterpref = EmployeeShiftInformationClass.EmployeeShiftInformation()
        mfilterpref.FilterShiftPreference(selectedoption)

mfp = ManagerFilterShiftPreferenceController.managerfilterpreference(selectedoption)