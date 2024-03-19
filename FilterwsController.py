import WorkShiftClass
import sys
import json

input_data = sys.argv[1]
x = json.loads(input_data)
selectedoption = x["selectedoption"]
value = x["value"]

class ManagerFilterWorkShift:
    def mFilterWorkShift(self, selectedoption, value):
        mfilterws = WorkShiftClass.WorkShift()
        mfilterws.ManagerFilterWorkShift(selectedoption, value)

mfilterws = ManagerFilterWorkShift.ManagerFilterWorkShift(selectedoption, value)