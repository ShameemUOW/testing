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
chatid = x["chatid"]
max = x["Maxhrs"]


class AdminCreateEmployeeAccountController:
    def createemployeeaccount(fullname,address,email,phonenumber,username,password,chatid,max):
        createemployee = UserAccountClass.userAccount()
        createemployee.createEmployeeAccount(fullname,address,email,phonenumber,username,password,chatid,max)

createemployee = AdminCreateEmployeeAccountController.createemployeeaccount(fullname,address,email,phonenumber,username,password,chatid,max)