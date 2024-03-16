import WorkShiftClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
id = x["id"]

class DeletewsController:
    def managerdeleteworkshift(id):
        mdws = WorkShiftClass.WorkShift()
        mdws.ManagerDeleteWorkShifts(id)

mdws = DeletewsController.managerdeleteworkshift(id)