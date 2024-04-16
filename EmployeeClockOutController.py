import AttendanceClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeId"]
currentTime = x["currentTime"]


class EmployeeClockOutController:
    def EmployeeClockOut(employeeid,currentTime):
        eco = AttendanceClass.Attendance()
        eco.EmployeeClockOut(employeeid,currentTime)

eco = EmployeeClockOutController.EmployeeClockOut(employeeid,currentTime)