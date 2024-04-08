import json
import random
from datetime import datetime, timedelta
import mysql.connector


mydb = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password='root',
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()
mycursor.execute("use FYP;")

class EmployeeShift:
    def __init__(self):
        pass
    def ManagerManualAssignEmployees(self, id, date,shifttype):
        try:
            # Check if the shift exists
            mycursor.execute("SELECT id FROM workshift WHERE Date = %s AND shift = %s", (date, shifttype))
            shift_record = mycursor.fetchone()

            if shift_record:
                shift_id = shift_record[0]
                # Insert the employee shift
                mycursor.execute("INSERT INTO EmployeeShift (shiftID, EmployeeID, shiftDate, shiftType) VALUES (%s, %s, %s, %s)",
                                (shift_id, id, date, shifttype))
                mydb.commit()
                print("Employee shift assigned successfully.")
            else:
                print("Shift does not exist.")

        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
    def auto_assign_employees(start_date, end_date, num_employees):
        try:

            # Retrieve workshifts within the specified date range
            query = "SELECT * FROM workshift WHERE Date BETWEEN %s AND %s"
            mycursor.execute(query, (start_date, end_date))
            workshifts = mycursor.fetchall()

            unassigned_shifts = []
            assigned_employees = []

            for shift in workshifts:
                shift_id, shift_date, shift_type, shift_start, shift_end = shift
                shift_duration = (datetime.strptime(shift_end, '%H:%M:%S') - datetime.strptime(shift_start, '%H:%M:%S')).seconds / 3600

                # Filter suitable employees for each shift
                query = """
                    SELECT * FROM EmployeeShiftInformation 
                    WHERE Day = %s AND ShiftPref = %s AND EmployeeID NOT IN (
                        SELECT EmployeeID FROM EmployeeLeave WHERE Date = %s
                    ) ORDER BY NoOfHrsWorked ASC
                """
                mycursor.execute(query, (shift_date, shift_type, shift_date))
                employees_available = mycursor.fetchall()

                if len(employees_available) < num_employees:
                    # If not enough employees available, add to unassigned shifts
                    unassigned_shifts.append({'date': shift_date, 'type': shift_type, 'needed': num_employees - len(employees_available)})
                else:
                    # Assign employees to the shift
                    num_to_assign = min(len(employees_available), num_employees)
                    selected_employees = random.sample(employees_available, num_to_assign)
                    for employee in selected_employees:
                        assigned_employees.append(employee)
                        employees_available.remove(employee)
                        # Insert assigned employee into EmployeeShift table
                        insert_query = "INSERT INTO EmployeeShift (shiftID, EmployeeID, shiftDate, shiftType) VALUES (%s, %s, %s, %s)"
                        mycursor.execute(insert_query, (shift_id, employee[0], shift_date, shift_type))
                        # Update EmployeeShiftInformation table
                        update_query = "UPDATE EmployeeShiftInformation SET NoOfHrsWorked = NoOfHrsWorked + %s WHERE EmployeeID = %s"
                        mycursor.execute(update_query, (shift_duration, employee[0]))

            mydb.commit()

            output = {'assigned_employees': assigned_employees, 'unassigned_shifts': unassigned_shifts}
            print(json.dumps(output))

        except Exception as e:
            print("Error while connecting to MySQL",str(e))
