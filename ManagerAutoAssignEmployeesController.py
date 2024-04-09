import EmployeeShiftClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
start = x["start"]
end = x["end"]
noe = x["numberofemployees"]


class ManagerAutoAssignEmployeesController:
    def ManagerAutoAssignEmployeeController(start, end, noe):
        maaec = EmployeeShiftClass.EmployeeShift()
        maaec.ManagerAutoAssignEmployees(start, end, noe)

maaec = ManagerAutoAssignEmployeesController.ManagerAutoAssignEmployeeController(start, end, noe)