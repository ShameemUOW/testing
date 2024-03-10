import UserAccountClass
import sys
import json

input = sys.argv[1]
y=json.loads(input)

username = y["username"]
password = y["password"]
mainrole = y["mainrole"]

class LoginController:
    def ValidateAccountDetails(username,password,mainrole):
        useraccount = UserAccountClass.UserAccount()
        print(useraccount.Login(username,password,mainrole))

LogginUserIn = LoginController.ValidateAccountDetails(username,password,mainrole)