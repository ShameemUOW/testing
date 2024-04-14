import json
import random
from datetime import datetime, timedelta
import mysql.connector
import NotificationClass
import threading
from time import sleep


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
                mycursor.execute("SELECT Email FROM userAccount WHERE EmployeeID = %s", (id,))
                employee_email = mycursor.fetchone()[0]
                email_thread = threading.Thread(target=self.send_email_for_ws, args=(employee_email, shifttype, date))
                email_thread.start()
                print("Employee shift assigned successfully.")
            else:
                print("Shift does not exist.")

        except Exception as e:
            print("Error while connecting to MySQL", e)
    def send_email_for_ws(self, recipient_email, shifttype, date):
        try:
            notification = NotificationClass.Notification()
            notification.send_email_for_ws(recipient_email, shifttype, date)
        except Exception as e:
            print(e)
    def ManagerAutoAssignEmployees(self, start_date, end_date, num_employees_per_shift):
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
                        SELECT EmployeeID FROM ApprovedEmployeeLeave WHERE Date = %s
                    )
                    AND w.Date = %s 
                    AND esi.NoofHrsWorked < 44
                    ORDER BY esi.NoOfHrsWorked ASC
                """
                mycursor.execute(query, (day_mapping[shift_day_of_week], shift_type, shift_date,shift_date))
                employees_available = mycursor.fetchall()
                if len(employees_available) < int(num_employees_per_shift):
                    # If not enough employees available, add to unassigned shifts
                    unassigned_shifts.append((shift_date, shift_type, (int(num_employees_per_shift) - len(employees_available))))
                else:
                    assigned_employee_ids = []  # List to keep track of assigned employee IDs
                    while len(assigned_employee_ids) < int(num_employees_per_shift):
                        # Remove already assigned employees from the available employees list
                        filtered_employees = [employee for employee in employees_available if employee[0] not in assigned_employee_ids]
                        if len(filtered_employees) > 0:
                            # Select a random employee from the filtered list
                            selected_employee = random.choice(filtered_employees)
                            assigned_employee_ids.append(selected_employee[0])
                            # Extract hours and minutes from timedelta for start and end
                            start_hours = shift_start.seconds // 3600
                            start_minutes = (shift_start.seconds % 3600) // 60

                            end_hours = shift_end.seconds // 3600
                            end_minutes = (shift_end.seconds % 3600) // 60

                            # Format as 'HH:MM'
                            shift_start_regular = '{:02}:{:02}'.format(start_hours, start_minutes)
                            shift_end_regular = '{:02}:{:02}'.format(end_hours, end_minutes)
                            assigned_employees.append((selected_employee[0], selected_employee[1], selected_employee[2], shift_date, shift_type, shift_start_regular, shift_end_regular))
                            # Insert assigned employee into EmployeeShift table
                            insert_query = "INSERT INTO EmployeeShift (shiftID, EmployeeID, shiftDate, shiftType) VALUES (%s, %s, %s, %s)"
                            mycursor.execute(insert_query, (shift_id, selected_employee[0], shift_date, shift_type))
                            notification = NotificationClass.Notification()
                            mycursor.execute("SELECT Email FROM userAccount WHERE EmployeeID = %s", (selected_employee[0],))
                            employee_email = mycursor.fetchone()[0]
                            notification.send_email_for_ws(employee_email, shift_type, shift_date)
                            # Update EmployeeShiftInformation table
                            update_query = "UPDATE EmployeeShiftInformation SET NoOfHrsWorked = NoOfHrsWorked + %s WHERE EmployeeID = %s"
                            mycursor.execute(update_query, (shift_duration, selected_employee[0]))
                        else:
                            break

            mydb.commit()
            mycursor.close()
            mydb.close()
            output = {'assigned_employees': assigned_employees, 'unassigned_shifts': unassigned_shifts}
            output_json = json.dumps(output)
            print(output_json)
        except Exception as e:
            print(e)
    def AdminViewFutureWorkshift(self,employeeid):
        try:
            today = datetime.now().date()
            date_str = today.strftime('%Y-%m-%d')
            mycursor.execute("SELECT * FROM EmployeeShift WHERE employeeid = %s AND shiftDate > %s", (employeeid, date_str))
            shifts = mycursor.fetchall()

            formatted_shifts = []
            for shift in shifts:
                formatted_shift = [shift[0],  shift[1],shift[2] , shift[3].strftime('%Y-%m-%d'), shift[4]]
                formatted_shifts.append(formatted_shift)

            shifts_json = json.dumps(formatted_shifts)
            print(shifts_json)
        except Exception as e:
            error_message = {"error": str(e)}
            print(json.dumps(error_message))
    def AdminReassignWorkShift(self,employeeid,id):
        try:
            mycursor.execute("Update EmployeeShift set employeeid = %s where employeeshiftid = %s", (employeeid, id))
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")