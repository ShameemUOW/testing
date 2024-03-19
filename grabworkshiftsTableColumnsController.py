import WorkShiftClass

class grabWorkShiftsTableColumnsController:
    def grabWorkShiftTableColumns():
        gwsd = WorkShiftClass.WorkShift()
        gwsd.grabworkshiftdetail()

gwsd = grabWorkShiftsTableColumnsController.grabWorkShiftTableColumns()