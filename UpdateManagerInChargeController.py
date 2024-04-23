import UserAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)

employeeid = x["employeeid"]


class UpdateManagerInChargeController:
    def UpdateManagerInChargeController(employeeid):
        update = UserAccountClass.UserAccount()
        update.SetManagerInCharge(employeeid)

uma = UpdateManagerInChargeController.UpdateManagerInChargeController(employeeid)