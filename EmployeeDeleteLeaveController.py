import EmployeeLeaveClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
id = x["id"]

class EmployeeDeleteLeaveController:
    def EmployeeDeleteLeaveController(id):
        mdws = EmployeeLeaveClass.EmployeeLeave()
        mdws.EmployeeDeleteLeave(id)

mdws = EmployeeDeleteLeaveController.EmployeeDeleteLeaveController(id)