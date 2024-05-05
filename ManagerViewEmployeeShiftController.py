import EmployeeShiftClass

class ManagerViewEmployeeShiftController:
    def ManagerViewEmployeeShift():
        managervc = EmployeeShiftClass.EmployeeShift()
        managervc.ViewEmployeeWorkShift()

mvc = ManagerViewEmployeeShiftController.ManagerViewEmployeeShift()