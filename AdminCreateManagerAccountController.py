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
password = x["password"]
chatid = x["chatid"]
max = x["Maxhrs"]

class AdminCreateManagerAccountController:
    def createmanageraccount(fullname,address,email,phonenumber,username,password,chatid,max):
        createmanager = userAccountClass.userAccount()
        createmanager.createManagerAccount(fullname,address,email,phonenumber,username,password,chatid,max)

createmanager = AdminCreateManagerAccountController.createmanageraccount(fullname,address,email,phonenumber,username,password,chatid,max)