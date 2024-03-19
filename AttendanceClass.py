import mysql.connector
import json
from datetime import datetime, timedelta

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()
mycursor.execute("use FYP;")

class Attendance:
    def __init__(self):
        pass
    def ManagerViewAttendance(self):
        try:
            mycursor.execute("SELECT * FROM attendance;")
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if numberofrow == 0:
                print("No table left")
            else:
                result = []
                for row in data:
                    leaveDate = row[2].strftime('%Y-%m-%d') if row[2] is not None else None
                    start_time = (datetime.min + row[3]).time().strftime('%H:%M:%S') if row[3] is not None else None
                    end_time = (datetime.min + row[4]).time().strftime('%H:%M:%S') if row[4] is not None else None
                    result.append((row[0], row[1], leaveDate, start_time, end_time, row[5]))
                print(json.dumps(result))
        except mysql.connector.Error as error:
            print("Failed to fetch data:", error)
    def grabAttendanceTableColumns(self):
        mycursor.execute("select column_name from information_schema.columns where table_schema = 'FYP' and table_name = 'Attendance' and column_name not in ('ClockIn','ClockOut')")
        data = mycursor.fetchall()
        result = json.dumps(data)
        print(result)
    def ManagerFilterAttendance(self, selectedoption,value):
        try:
            mycursor.execute("select * from Attendance where {} LIKE '%{}%';'".format(selectedoption,value))
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = []
                for row in data:
                    leaveDate = row[2].strftime('%Y-%m-%d') if row[2] is not None else None
                    start_time = (datetime.min + row[3]).time().strftime('%H:%M:%S') if row[3] is not None else None
                    end_time = (datetime.min + row[4]).time().strftime('%H:%M:%S') if row[4] is not None else None
                    result.append((row[0], row[1], leaveDate, start_time, end_time, row[5]))
                print(json.dumps(result))
        except mysql.connector.Error as error:
            print("Failed to fetch data:", error)
    def EmployeeClockIn(self, employeeid,shiftid,datein,timein):
        try:
            # Parse date and time strings into datetime objects
            date_obj = datetime.strptime(datein, "%d/%m/%Y")
            time_obj = datetime.strptime(timein, "%I:%M:%S %p")

            # Check if the provided shift ID exists for the employee
            mycursor.execute("SELECT * FROM EmployeeShift WHERE shiftID = %s AND EmployeeID = %s", (shiftid, employeeid))
            shift_record = mycursor.fetchone()
            if not shift_record:
                raise ValueError("The provided shift ID does not exist for the employee.")

            # Retrieve the start time of the shift from the workshift table
            mycursor.execute("SELECT start FROM workshift WHERE id = %s", (shiftid,))
            shift_start_time = mycursor.fetchone()[0]

            # Convert shift_start_time to a time object
            shift_start_time = datetime.strptime(str(shift_start_time), "%H:%M:%S").time()

            # Combine date and time into a datetime object
            clock_in_datetime = datetime.combine(date_obj, time_obj.time())

            # Compare clock-in time with shift start time and insert into attendance table accordingly
            if clock_in_datetime.time() > shift_start_time:
                mycursor.execute("INSERT INTO attendance (EmployeeID, Date, ClockIn, Attendance) VALUES (%s, %s, %s, %s)", (employeeid, date_obj.strftime("%Y-%m-%d"), time_obj.strftime("%H:%M:%S"), 'Late'))
            else:
                mycursor.execute("INSERT INTO attendance (EmployeeID, Date, ClockIn, Attendance) VALUES (%s, %s, %s, %s)", (employeeid, date_obj.strftime("%Y-%m-%d"), time_obj.strftime("%H:%M:%S"), 'On time'))

            # Commit changes to the database
            mydb.commit()
            return "Clock in successful."
        except mysql.connector.Error as error:
            print("Failed to execute query:", error)
            return "Failed Attendance Class"
        except ValueError as e:
            print("Error:", e)
            return "Failed Attendance Class"