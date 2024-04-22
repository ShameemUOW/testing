import userAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
selectedoption = x["selectedoption"]
value = x["value"]


class AdminSearchAdminAccountController:
    def searchadminaccount(selectedoption,value):
        searchadmin = userAccountClass.userAccount()
        searchadmin.searchAdminAccount(selectedoption,value)

searchadmin = AdminSearchAdminAccountController.searchadminaccount(selectedoption,value)