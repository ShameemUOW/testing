import EmployeeShiftClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]
id = x["id"]

class AdminReassignWorkShiftsController:
    def AdminReassignWorkShiftsController(employeeid,id):
        avfsc = EmployeeShiftClass.EmployeeShift()
        avfsc.AdminReassignWorkShift(employeeid,id)

avfsc = AdminReassignWorkShiftsController.AdminReassignWorkShiftsController(employeeid,id)