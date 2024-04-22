import UserProfileClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]
selectedoption = x["selectedoption"]
role = x["role"]

class UpdateuserProfileController:
    def updateuserProfile(employeeid,selectedoption,role):
        updateprofile = UserProfileClass.userProfile()
        updateprofile.updateuserProfile(employeeid,selectedoption,role)

createuaccount = UpdateuserProfileController.updateuserProfile(employeeid,selectedoption,role)