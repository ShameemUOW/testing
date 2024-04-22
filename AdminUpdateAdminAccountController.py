import UserAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]
selectedoption = x["selectedoption"]
value = x["value"]

class AdminUpdateAdminAccountController:
    def AdminUpdateAdminAccountController(employeeid,selectedoption,value):
        adminupdateadminacc = UserAccountClass.userAccount()
        adminupdateadminacc.AdminUpdateAdminAccount(employeeid,selectedoption,value)

auda = AdminUpdateAdminAccountController.AdminUpdateAdminAccountController(employeeid,selectedoption,value)