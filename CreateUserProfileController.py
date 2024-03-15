import UserProfileClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]
profile = x["profile"]
role = x["role"]

class CreateUserProfileController:
    def createuserprofile(employeeid,profile,role):
        createaccount = UserProfileClass.UserProfile()
        createaccount.createUserProfile(employeeid,profile,role)

createuaccount = CreateUserProfileController.createuserprofile(employeeid,profile,role)