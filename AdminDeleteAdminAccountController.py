import userAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]

class AdminDeleteAdminAccountController:
    def deleteadminaccount(employeeid):
        deleteadmin = userAccountClass.userAccount()
        deleteadmin.DeleteAdminAccount(employeeid)

deleteadmin = AdminDeleteAdminAccountController.deleteadminaccount(employeeid)