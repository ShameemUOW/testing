import AttendanceClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeId"]

class EmployeeViewPastWorkHistoryController:
    def EmployeeViewPastWorkHistoryController(employeeid):
        pasthis = AttendanceClass.Attendance()
        pasthis.EmployeeViewPastWorkHistory(employeeid)

pasthis = EmployeeViewPastWorkHistoryController.EmployeeViewPastWorkHistoryController(employeeid)