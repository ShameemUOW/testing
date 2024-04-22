import UserAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]

class AdminDeleteManagerAccountController:
    def deleteManageraccount(employeeid):
        deletemanager = UserAccountClass.userAccount()
        deletemanager.DeleteManagerAccount(employeeid)

deletemanager = AdminDeleteManagerAccountController.deleteManageraccount(employeeid)