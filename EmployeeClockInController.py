import AttendanceClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeId"]
currentDate = x["currentDate"]
currentTime = x["currentTime"]


class EmployeeClockInController:
    def EmployeeClockIn(employeeid,currentDate,currentTime):
        mdws = AttendanceClass.Attendance()
        mdws.EmployeeClockIn(employeeid,currentDate,currentTime)

mdws = EmployeeClockInController.EmployeeClockIn(employeeid,currentDate,currentTime)