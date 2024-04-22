import userAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
selectedoption = x["selectedoption"]
value = x["value"]


class AdminFilterAdminAccountController:
    def filteradminaccount(selectedoption,value):
        filteradmin = userAccountClass.userAccount()
        filteradmin.filterAdminAccount(selectedoption,value)

filteradmin = AdminFilterAdminAccountController.filteradminaccount(selectedoption,value)