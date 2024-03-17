import EmployeeLeaveClass
import sys
import json

try:
    input2 = sys.argv[1]
except IndexError:
    print("Error: No command-line argument provided.")
    sys.exit(1)

z = json.loads(input2)
fullname = z["fullname"]
date = z["date"]
leavetype = z["leavetype"]

class CreateEmployeeLeaveController:
    @staticmethod
    def create_employeeleave(fullname, date, leavetype):
        employeeleave = EmployeeLeaveClass.EmployeeLeave()
        employeeleave.CreateEmployeeLeave(fullname, date, leavetype)

CreateEmployeeLeaveController.create_employeeleave(fullname, date, leavetype)