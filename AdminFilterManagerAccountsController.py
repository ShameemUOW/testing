import UserAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
selectedoption = x["selectedoption"]
value = x["value"]


class AdminFilterManagerAccountController:
    def filtermanageraccount(selectedoption,value):
        filtermanager = UserAccountClass.userAccount()
        filtermanager.filterManagerAccount(selectedoption,value)

filtermanager = AdminFilterManagerAccountController.filtermanageraccount(selectedoption,value)