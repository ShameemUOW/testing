import EmployeeShiftClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]

class EmployeeViewShiftsController:
    def EmployeeViewShiftsController(employeeid):
        avfsc = EmployeeShiftClass.EmployeeShift()
        avfsc.EmployeeViewShifts(employeeid)

avfsc = EmployeeViewShiftsController.EmployeeViewShiftsController(employeeid)