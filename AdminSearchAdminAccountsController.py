import UserAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
selectedoption = x["selectedoption"]
value = x["value"]


class AdminSearchAdminAccountController:
    def searchadminaccount(selectedoption,value):
        searchadmin = UserAccountClass.UserAccount()
        searchadmin.searchAdminAccount(selectedoption,value)

searchadmin = AdminSearchAdminAccountController.searchadminaccount(selectedoption,value)