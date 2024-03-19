import AttendanceClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]
currentDate = x["currentDate"]
currentTime = x["currentTime"]
shiftid = x["shiftid"]


class EmployeeClockInController:
    def EmployeeClockIn(employeeid,shiftid,currentDate,currentTime):
        mdws = AttendanceClass.Attendance()
        mdws.EmployeeClockIn(employeeid,shiftid,currentDate,currentTime)

mdws = EmployeeClockInController.EmployeeClockIn(employeeid,shiftid,currentDate,currentTime)