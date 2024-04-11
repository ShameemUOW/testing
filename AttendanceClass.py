import mysql.connector
import json
from datetime import datetime

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
    def EmployeeClockIn(self, employeeid, shiftid, datein, timein):
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
            mycursor.execute("SELECT date, start FROM workshift WHERE id = %s", (shiftid,))
            shift_date_obj, shift_start_time = mycursor.fetchone()

            shift_date_obj = datetime.strptime(shift_date_obj, "%Y-%m-%d").date()
            # Convert shift_start_time to a time object
            shift_start_time = datetime.strptime(str(shift_start_time), "%H:%M:%S").time()

            # Combine date and time into a datetime object
            clock_in_datetime = datetime.combine(date_obj, time_obj.time())
            shiftstartdatetime = datetime.combine(shift_date_obj, shift_start_time)
            time_difference = shiftstartdatetime - clock_in_datetime

            # Check if the clock-in time is more than 2 hours before the shift start time
            if time_difference.total_seconds() > 7200:  # 2 hours in seconds
                raise ValueError("You cannot clock in more than 2 hours before the shift start time.")

            # Compare clock-in time with shift start time and insert into attendance table accordingly
            if clock_in_datetime > shiftstartdatetime:
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
    def EmployeeClockOut(self, employeeid,timeout):
        time_obj = datetime.strptime(timeout, "%I:%M:%S %p")
        formatted_time = time_obj.strftime("%H:%M:%S")
        try:
            mycursor.execute("SELECT AttendanceID FROM Attendance WHERE EmployeeID = %s AND ClockOut IS NULL",(employeeid,))
            unclocked_entry = mycursor.fetchone()
            if unclocked_entry:
                attendance_id = unclocked_entry[0]
                mycursor.execute("UPDATE Attendance SET ClockOut = %s WHERE AttendanceID = %s",(formatted_time,attendance_id,))
                mydb.commit()
                print("Clock-out time updated successfully.")
            else:
                print("No unclocked entry found for the employee.")
        except mysql.connector.Error as error:
            print("Failed to update clock-out time:", error)
    def EmployeeViewPastWorkHistory(self,employeeid):
        try:
            mycursor.execute("SELECT Date,ClockIn,ClockOut,Attendance FROM attendance where employeeid = '{}';".format(employeeid))
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if numberofrow == 0:
                print("No table left")
            else:
                result = []
                for row in data:
                    date = row[0].strftime('%Y-%m-%d') if row[0] is not None else None
                    clockin = (datetime.min + row[1]).time().strftime('%H:%M:%S') if row[1] is not None else None
                    clockout = (datetime.min + row[2]).time().strftime('%H:%M:%S') if row[2] is not None else None
                    result.append((date, clockin, clockout, row[3]))
                print(json.dumps(result))
        except mysql.connector.Error as error:
            print("Failed to fetch data:", error)

