import UserAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
selectedoption = x["selectedoption"]
value = x["value"]


class AdminSearchEmployeeAccountController:
    def searchemployeeaccount(selectedoption,value):
        searchemployee = UserAccountClass.UserAccount()
        searchemployee.searchEmployeeAccount(selectedoption,value)

searchEmployee = AdminSearchEmployeeAccountController.searchemployeeaccount(selectedoption,value)