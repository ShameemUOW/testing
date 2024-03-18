import AttendanceClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
selectedoption = x["selectedoption"]
value = x["value"]

class ManagerFilterAttendance:
    def ManagerFilterAttendanceController(selectedoption,value):
        mfacc = AttendanceClass.Attendance()
        mfacc.ManagerFilterAttendance(selectedoption,value)

mfacc = ManagerFilterAttendance.ManagerFilterAttendanceController(selectedoption,value)