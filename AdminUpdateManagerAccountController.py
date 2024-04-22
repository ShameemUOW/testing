import UserAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]
selectedoption = x["selectedoption"]
value = x["value"]

class AdminUpdateManagerAccountController:
    def AdminUpdateManagerAccountController(employeeid,selectedoption,value):
        adminupdatemanacc = UserAccountClass.userAccount()
        adminupdatemanacc.AdminUpdateManagerAccount(employeeid,selectedoption,value)

auma = AdminUpdateManagerAccountController.AdminUpdateManagerAccountController(employeeid,selectedoption,value)