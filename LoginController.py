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
        userAccount = UserAccountClass.userAccount()
        print(userAccount.Login(username,password,mainrole))

LogginUserIn = LoginController.ValidateAccountDetails(username,password,mainrole)