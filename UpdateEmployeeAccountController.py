import UserAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)

employeeid = x["employeeid"]
selectedoption = x["selectedoption"]
value = x["value"]


class UpdateEmployeeAccountController:
    def updateEmployeeAccount(employeeid,selectedoption,value):
        update = UserAccountClass.UserAccount()
        update.updateEmployeeAccount(employeeid,selectedoption,value)

uma = UpdateEmployeeAccountController.updateEmployeeAccount(employeeid,selectedoption,value)
