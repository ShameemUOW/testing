import EmployeeLeaveClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
id = x["id"]

class ManagerApproveLeave:
    def ManagerApproveLeaveController(id):
        mdws = EmployeeLeaveClass.EmployeeLeave()
        mdws.ManagerApproveLeave(id)

mdws = ManagerApproveLeave.ManagerApproveLeaveController(id)