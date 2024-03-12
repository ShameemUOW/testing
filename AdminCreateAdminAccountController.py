import UserAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
fullname = x["fullname"]
address = x["address"]
email = x["email"]
phonenumber = x["phonenumber"]
username = x["username"]
password = x["password"]
max = x["Maxhrs"]


class AdminCreateAdminAccountController:
    def createadminaccount(fullname,address,email,phonenumber,username,password,max):
        createadmin = UserAccountClass.UserAccount()
        createadmin.createAdminAccount(fullname,address,email,phonenumber,username,password,max)

createadmin = AdminCreateAdminAccountController.createadminaccount(fullname,address,email,phonenumber,username,password,max)