import userAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)

employeeid = x["employeeid"]
selectedoption = x["selectedoption"]
value = x["value"]


class UpdateManagerAccountController:
    def updateManagerAccount(employeeid,selectedoption,value):
        update = userAccountClass.userAccount()
        update.updateManagerAccount(employeeid,selectedoption,value)

uma = UpdateManagerAccountController.updateManagerAccount(employeeid,selectedoption,value)
