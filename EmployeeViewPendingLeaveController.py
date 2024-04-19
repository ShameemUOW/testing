import EmployeeLeaveClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]

class EmployeeViewPendingLeavesController:
    def EmployeeViewPendingLeavesController(employeeid):
        mdws = EmployeeLeaveClass.EmployeeLeave()
        mdws.EmployeeViewPendingLeave(employeeid)

mdws = EmployeeViewPendingLeavesController.EmployeeViewPendingLeavesController(employeeid)