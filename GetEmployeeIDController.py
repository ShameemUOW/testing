import UserAccountClass
import sys
import json

input = sys.argv[1]
y=json.loads(input)

username = y["username"]
password = y["password"]
mainrole = y["mainrole"]

class GetEmployeeIDController:
    def getemployeeid(username,password,mainrole):
        userAccount = UserAccountClass.userAccount()
        userAccount.getEmployeeID(username,password,mainrole)

gettingemployeeid = GetEmployeeIDController.getemployeeid(username,password,mainrole)