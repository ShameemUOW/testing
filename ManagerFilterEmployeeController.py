import userAccountClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
selectedoption = x["selectedoption"]
value = x["value"]

class ManagerFilterEmployeeAccount:
    def mFiltergrabEmployeeAccounts(selectedoption,value):
        mfgtc = userAccountClass.userAccount()
        mfgtc.ManagerFilterEmployees(selectedoption,value)

mfgtc = ManagerFilterEmployeeAccount.mFiltergrabEmployeeAccounts(selectedoption,value)