import UserAccountClass
import sys
import json

try:
    input2 = sys.argv[1]
except IndexError:
    print("Error: No command-line argument provided.")
    sys.exit(1)

z = json.loads(input2)
employeeId = z["employeeId"]

class EmployeeViewAccount:
    def EmployeeViewAccountController():
        employeeviewac = UserAccountClass.userAccount()
        employeeviewac.EmployeeViewAccount(employeeId)

avup = EmployeeViewAccount.EmployeeViewAccountController()