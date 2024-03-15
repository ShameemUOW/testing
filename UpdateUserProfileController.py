import UserProfileClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]
selectedoption = x["selectedoption"]
role = x["role"]

class UpdateUserProfileController:
    def updateuserprofile(employeeid,selectedoption,role):
        updateprofile = UserProfileClass.UserProfile()
        updateprofile.updateUserProfile(employeeid,selectedoption,role)

createuaccount = UpdateUserProfileController.updateuserprofile(employeeid,selectedoption,role)