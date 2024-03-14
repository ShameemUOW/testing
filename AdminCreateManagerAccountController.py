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

class AdminCreateManagerAccountController:
    def createmanageraccount(fullname,address,email,phonenumber,username,password,max):
        createmanager = UserAccountClass.UserAccount()
        createmanager.createManagerAccount(fullname,address,email,phonenumber,username,password,max)

createmanager = AdminCreateManagerAccountController.createmanageraccount(fullname,address,email,phonenumber,username,password,max)