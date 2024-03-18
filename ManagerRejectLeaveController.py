import EmployeeLeaveClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
id = x["id"]

class ManagerRejectLeave:
    def ManagerRejectLeaveController(id):
        mdws = EmployeeLeaveClass.EmployeeLeave()
        mdws.ManagerRejectLeave(id)

mdws = ManagerRejectLeave.ManagerRejectLeaveController(id)