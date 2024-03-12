import UserAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)

fullname = x["fullname"]
email = x["email"]
phonenumber = x["phonenumber"]
username = x["username"]
password = x["password"]
max = x["Maxhrs"]


class UpdateManagerAccountController:
    def updateManagerAccount(fullname,email,password,mobile,username,MaxHours):
        update = UserAccountClass.UserAccount()
        update.updateManagerAccount(fullname,email,password,mobile,username,MaxHours)

