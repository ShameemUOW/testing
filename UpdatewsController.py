import WorkShiftClass
import sys
import json

input = sys.argv[1]
print("Received JSON data:", input)  # Add this line to check what data is received
x = json.loads(input)

id = x["id"]
selectedoption = x["selectedoption"]
value = x["value"]


class UpdateWsController:
    def updateWorkShift(id,selectedoption,value):
        uwsc = WorkShiftClass.WorkShift()
        uwsc.updateWorkShift(id,selectedoption,value)

uwsc = UpdateWsController.updateWorkShift(id,selectedoption,value)