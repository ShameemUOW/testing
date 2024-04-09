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
    def ManagerAutoAssignEmployees(self,start_date, end_date, num_employees_per_shift):
        try:
            # Retrieve workshifts within the specified date range
            mycursor.execute("SELECT * FROM workshift WHERE Date BETWEEN '{}' AND '{}'".format(start_date, end_date))
            workshifts = mycursor.fetchall()
            unassigned_shifts = []
            assigned_employees = []

            for shift in workshifts:
                shift_id, shift_date, shift_type, shift_start, shift_end = shift
                shift_date_obj = datetime.strptime(shift_date, '%Y-%m-%d').date()
                shift_day_of_week = shift_date_obj.weekday()
                day_mapping = {
                    0: 'Monday',
                    1: 'Tuesday',
                    2: 'Wednesday',
                    3: 'Thursday',
                    4: 'Friday',
                    5: 'Saturday',
                    6: 'Sunday'
                }

                shift_duration = (shift_end - shift_start).total_seconds() / 3600
                # Filter suitable employees for each shift
                query = """
                    SELECT ua.EmployeeID, ua.Fullname, ua.Mobile, w.start, w.end 
                    FROM EmployeeShiftInformation esi
                    JOIN userAccount ua ON esi.EmployeeID = ua.EmployeeID
                    JOIN workshift w ON esi.ShiftPref = w.shift
                    WHERE esi.Day = %s AND esi.ShiftPref = %s AND esi.EmployeeID NOT IN (
                        SELECT EmployeeID FROM EmployeeLeave WHERE Date = %s
                    ) 
                    AND esi.NoOfHrsWorked <= 44 
                    ORDER BY esi.NoOfHrsWorked ASC
                """
                mycursor.execute(query, (day_mapping[shift_day_of_week], shift_type, shift_date))
                employees_available = mycursor.fetchall()
                if len(employees_available) < int(num_employees_per_shift):
                    # If not enough employees available, add to unassigned shifts
                    unassigned_shifts.append((shift_date,shift_type,(int(num_employees_per_shift) - len(employees_available))))
                else:
                    # Arrange employees based on hours worked in ascending order
                    employees_available.sort(key=lambda x: x[3])  # Assuming NoOfHrsWorked is at index 4
                    if len(employees_available) >= 5:
                        # Randomly select 2 employees from the first 5
                        selected_employees = random.sample(employees_available[:5], int(num_employees_per_shift))
                    else:
                        # If fewer than 5 employees available, select 2 from all available employees
                        selected_employees = random.sample(employees_available, int(num_employees_per_shift))
                    for employee in selected_employees:
                        # Extract hours and minutes from timedelta for start and end
                        start_hours = shift_start.seconds // 3600
                        start_minutes = (shift_start.seconds % 3600) // 60

                        end_hours = shift_end.seconds // 3600
                        end_minutes = (shift_end.seconds % 3600) // 60

                        # Format as 'HH:MM'
                        shift_start_regular = '{:02}:{:02}'.format(start_hours, start_minutes)
                        shift_end_regular = '{:02}:{:02}'.format(end_hours, end_minutes)
                        assigned_employees.append((employee[0], employee[1], employee[2],shift_date,shift_type, shift_start_regular, shift_end_regular))
                        # Insert assigned employee into EmployeeShift table
                        insert_query = "INSERT INTO EmployeeShift (shiftID, EmployeeID, shiftDate, shiftType) VALUES (%s, %s, %s, %s)"
                        mycursor.execute(insert_query, (shift_id, employee[0], shift_date, shift_type))
                        # Update EmployeeShiftInformation table
                        update_query = "UPDATE EmployeeShiftInformation SET NoOfHrsWorked = NoOfHrsWorked + %s WHERE EmployeeID = %s"
                        mycursor.execute(update_query, (shift_duration, employee[0]))

            mydb.commit()
            mycursor.close()
            mydb.close()

            output = {'assigned_employees': assigned_employees, 'unassigned_shifts': unassigned_shifts}
            output_json = json.dumps(output)
            print(output_json)

        except Exception as e:
            print(e)