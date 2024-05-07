import EmployeeShiftClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]
id = x["id"]

class ManagerReassignWorkShiftsController:
    def ManagerReassignWorkShiftsController(employeeid,id):
        avfsc = EmployeeShiftClass.EmployeeShift()
        avfsc.ManagerReassignWorkShift(employeeid,id)

avfsc = ManagerReassignWorkShiftsController.ManagerReassignWorkShiftsController(employeeid,id)