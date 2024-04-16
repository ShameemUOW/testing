import EmployeeLeaveClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
id = x["id"]
reason = x["reason"]

class ManagerRejectLeave:
    def ManagerRejectLeaveController(id,reason):
        mdws = EmployeeLeaveClass.EmployeeLeave()
        mdws.ManagerRejectLeave(id,reason)

mdws = ManagerRejectLeave.ManagerRejectLeaveController(id,reason)