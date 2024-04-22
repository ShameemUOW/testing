import UserProfileClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]
profile = x["profile"]
role = x["role"]

class CreateuserProfileController:
    def createuserProfile(employeeid,profile,role):
        createaccount = UserProfileClass.userProfile()
        createaccount.createuserProfile(employeeid,profile,role)

createuaccount = CreateuserProfileController.createuserProfile(employeeid,profile,role)