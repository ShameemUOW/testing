import EmployeeLeaveClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)

selectedoption = x["selectedoption"]
value = x["value"]
leaveid = x["leaveid"]


class EmployeeUpdateLeaveController:
    def EmployeeUpdateLeaveController(leaveid,selectedoption,value):
        update = EmployeeLeaveClass.EmployeeLeave()
        update.EmployeeUpdateLeave(leaveid,selectedoption,value)

uma = EmployeeUpdateLeaveController.EmployeeUpdateLeaveController(leaveid,selectedoption,value)