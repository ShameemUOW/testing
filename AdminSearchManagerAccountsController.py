import userAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
selectedoption = x["selectedoption"]
value = x["value"]

class AdminSearchManagerAccountController:
    def searchmanageraccount(selectedoption,value):
        searchmanager = userAccountClass.userAccount()
        searchmanager.searchManagerAccount(selectedoption,value)

searchmanager = AdminSearchManagerAccountController.searchmanageraccount(selectedoption,value)