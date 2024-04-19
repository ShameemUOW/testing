import UserAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
selectedoption = x["selectedoption"]
value = x["value"]


class AdminFilterEmployeeAccountController:
    def filteremployeeaccount(selectedoption,value):
        filteremp = UserAccountClass.UserAccount()
        filteremp.filterEmployeeAccount(selectedoption,value)

filteremp = AdminFilterEmployeeAccountController.filteremployeeaccount(selectedoption,value)