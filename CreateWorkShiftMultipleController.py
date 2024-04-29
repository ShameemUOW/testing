import WorkShiftClass
import sys
import json

try:
    input2 = sys.argv[1]
except IndexError:
    print("Error: No command-line argument provided.")
    sys.exit(1)

z = json.loads(input2)
startdate = z["startdate"]
enddate = z["enddate"]
shift = z["shift"]
start = z["start"]
end = z["end"]

class CreateWorkShiftMultipleController:
    def CreateWorkShiftMultipleController(startdate,enddate, shift, start, end):
        createws = WorkShiftClass.WorkShift()
        createws.CreateMultipleWorkshifts(startdate,enddate, shift, start, end)

CreateWorkShiftMultipleController.CreateWorkShiftMultipleController(startdate,enddate, shift, start, end)