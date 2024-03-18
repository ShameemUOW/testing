import EmployeeLeaveClass

class ManagerViewPendingLeaves:
    def ManagerViewPendingLeavesController():
        managervpl = EmployeeLeaveClass.EmployeeLeave()
        managervpl.ManagerViewPendingLeave()

mvpl = ManagerViewPendingLeaves.ManagerViewPendingLeavesController()