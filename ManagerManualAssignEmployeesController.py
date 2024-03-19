import EmployeeShiftClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]
date = x["date"]
selectedoption = x ["selectedoption"]

class ManagerManualAssignEmployeesController:
    def ManagerManualAssignEmployees(employeeid,date,selectedoption):
        mmae = EmployeeShiftClass.EmployeeShift()
        mmae.ManagerManualAssignEmployees(employeeid,date,selectedoption)

mmae = ManagerManualAssignEmployeesController.ManagerManualAssignEmployees(employeeid,date,selectedoption)