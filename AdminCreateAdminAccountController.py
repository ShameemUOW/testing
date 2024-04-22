import userAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
fullname = x["fullname"]
address = x["address"]
email = x["email"]
phonenumber = x["phonenumber"]
username = x["username"]
chatid = x["chatid"]
password = x["password"]
max = x["Maxhrs"]


class AdminCreateAdminAccountController:
    def createadminaccount(fullname,address,email,phonenumber,username,password,chatid,max):
        createadmin = userAccountClass.userAccount()
        createadmin.createAdminAccount(fullname,address,email,phonenumber,username,password,chatid,max)

createadmin = AdminCreateAdminAccountController.createadminaccount(fullname,address,email,phonenumber,username,password,chatid,max)