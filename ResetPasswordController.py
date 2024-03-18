import UserAccountClass
import sys
import json

input = sys.argv[1]
y=json.loads(input)

password = y["password"]
employeeid = y["employeeid"]

class ResetPasswordController:
    def ResetPassword(password,employeeid):
        useraccount = UserAccountClass.UserAccount()
        print(useraccount.ResetPassword(password,employeeid))

LogginUserIn = ResetPasswordController.ResetPassword(password,employeeid)