import WorkShiftClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
selectedoption = x["selectedoption"]
value = x["value"]

class ManagerFilterWorkShift:
    def ManagerFilterWorkShiftController(selectedoption,value):
        mfws = WorkShiftClass.WorkShift()
        mfws.ManagerFilterWorkShift(selectedoption,value)

mfws = ManagerFilterWorkShift.ManagerFilterWorkShiftController(selectedoption,value)