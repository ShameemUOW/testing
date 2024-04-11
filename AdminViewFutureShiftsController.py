import EmployeeShiftClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]

class AdminViewFutureShiftsController:
    def AdminViewFutureShiftsController(employeeid):
        avfsc = EmployeeShiftClass.EmployeeShift()
        avfsc.AdminViewFutureWorkshift(employeeid)

avfsc = AdminViewFutureShiftsController.AdminViewFutureShiftsController(employeeid)