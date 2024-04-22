import UserAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
selectedoption = x["selectedoption"]
value = x["value"]

class ManagerSearchEmployeeAccount:
    def ManagerSearchEmployeeAccountController(selectedoption,value):
        mseac = UserAccountClass.userAccount()
        mseac.ManagerSearchEmployees(selectedoption,value)

mfgtc = ManagerSearchEmployeeAccount.ManagerSearchEmployeeAccountController(selectedoption,value)