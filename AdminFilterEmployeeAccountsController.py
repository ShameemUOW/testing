import userAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
selectedoption = x["selectedoption"]
value = x["value"]


class AdminFilterEmployeeAccountController:
    def filteremployeeaccount(selectedoption,value):
        filteremp = userAccountClass.userAccount()
        filteremp.filterEmployeeAccount(selectedoption,value)

filteremp = AdminFilterEmployeeAccountController.filteremployeeaccount(selectedoption,value)