import userAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]

class AdminDeleteEmployeeAccountController:
    def deleteemployeeaccount(employeeid):
        deleteemployee = userAccountClass.userAccount()
        deleteemployee.DeleteEmployeeAccount(employeeid)

deleteemployee = AdminDeleteEmployeeAccountController.deleteemployeeaccount(employeeid)