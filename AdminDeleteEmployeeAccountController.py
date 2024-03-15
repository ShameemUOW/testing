import UserAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]

class AdminDeleteEmployeeAccountController:
    def deleteemployeeaccount(employeeid):
        deleteemployee = UserAccountClass.UserAccount()
        deleteemployee.DeleteEmployeeAccount(employeeid)

deleteemployee = AdminDeleteEmployeeAccountController.deleteemployeeaccount(employeeid)