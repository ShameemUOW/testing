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


class AdminCreateEmployeeAccountController:
    def createemployeeaccount(fullname,address,email,phonenumber,username,password,max):
        createemployee = UserAccountClass.UserAccount()
        createemployee.createEmployeeAccount(fullname,address,email,phonenumber,username,password,max)

createemployee = AdminCreateEmployeeAccountController.createemployeeaccount(fullname,address,email,phonenumber,username,password,max)