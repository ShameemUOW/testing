import EmployeeShiftClass

class ViewCalenderFormatWorkController:
    def ViewCalenderFormatWork():
        managervc = EmployeeShiftClass.EmployeeShift()
        managervc.ViewCalenderFormatWork()

mvc = ViewCalenderFormatWorkController.ViewCalenderFormatWork()