import WorkShiftClass
import sys
import json

try:
    input2 = sys.argv[1]
except IndexError:
    print("Error: No command-line argument provided.")
    sys.exit(1)

z = json.loads(input2)
date = z["date"]
shift = z["shift"]
start = z["start"]
end = z["end"]

class CreatewsController:
    @staticmethod
    def create_workshift(date, shift, start, end):
        createws = WorkShiftClass.WorkShift()
        createws.createws(date, shift, start, end)

CreatewsController.create_workshift(date, shift, start, end)