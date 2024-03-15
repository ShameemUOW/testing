import WorkShiftClass
import sys
import json


input_data = sys.argv[1]
x = json.loads(input_data)
date = x["date"]
shift = x["shift"]
start = x["start"]
end = x["end"]

class CreatewsController:
    @staticmethod
    def createworkshift(date, shift, start, end):
        createws = WorkShiftClass.WorkShift()
        createws.createws(date, shift, start, end)

CreatewsController.createworkshift(date, shift, start, end)