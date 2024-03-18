import EmployeeLeaveClass
import sys
import json

try:
    input2 = sys.argv[1]
except IndexError:
    print("Error: No command-line argument provided.")
    sys.exit(1)

z = json.loads(input2)
employeeId = z["employeeId"]
date = z["date"]
leavetype = z["leavetype"]

class CreateEmployeeLeaveController:
    @staticmethod
    def create_employeeleave(employeeId, date, leavetype):
        employeeleave = EmployeeLeaveClass.EmployeeLeave()
        employeeleave.CreateEmployeeLeave(employeeId, date, leavetype)

CreateEmployeeLeaveController.create_employeeleave(employeeId, date, leavetype)