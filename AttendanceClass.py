import mysql.connector
import json
from datetime import datetime

class Attendance:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host ='bdpspl67hpsxmkiiukdu-mysql.services.clever-cloud.com',
            user ='u5fgsonwyoke5bff',
            password='nHsZUdEJQ30AYtYXN6nF',
            database='bdpspl67hpsxmkiiukdu',
            port = '3306'
        )
        self.mycursor = self.mydb.cursor()
    def ManagerViewAttendance(self):
        try:
            self.mycursor.execute("SELECT * FROM Attendance;")
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
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
        finally:
            self.mydb.close()
    def grabAttendanceTableColumns(self):
        self.mycursor.execute("select column_name from information_schema.columns where table_schema = 'bdpspl67hpsxmkiiukdu' and table_name = 'Attendance' and column_name not in ('ClockIn','ClockOut')")
        data = self.mycursor.fetchall()
        result = json.dumps(data)
        self.mydb.close()
        print(result)
    def ManagerFilterAttendance(self, selectedoption,value):
        try:
            self.mycursor.execute("select * from Attendance where {} LIKE '%{}%';'".format(selectedoption,value))
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
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
        finally:
            self.mydb.close()
    def EmployeeClockIn(self, employeeid, datein, timein):
        try:
            # Parse date and time strings into datetime objects
            date_obj = datetime.strptime(datein, "%d/%m/%Y")
            time_obj = datetime.strptime(timein, "%I:%M:%S %p")

            # Check if the provided shift ID exists for the employee
            self.mycursor.execute("SELECT * FROM EmployeeShift WHERE shiftDate = %s AND EmployeeID = %s", (date_obj.strftime("%Y-%m-%d"), employeeid))
            shift_record = self.mycursor.fetchone()
            if shift_record:
                shiftID = shift_record[1]
            elif not shift_record:
                raise ValueError("The provided shift does not exist for the employee.")
            

            # Retrieve the start time of the shift from the workshift table
            self.mycursor.execute("SELECT date, start FROM workshift WHERE id = %s", (shiftID,))
            shift_date_obj, shift_start_time = self.mycursor.fetchone()

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
                self.mycursor.execute("INSERT INTO Attendance (EmployeeID, Date, ClockIn, Attendance) VALUES (%s, %s, %s, %s)", (employeeid, date_obj.strftime("%Y-%m-%d"), time_obj.strftime("%H:%M:%S"), 'Late'))
            else:
                self.mycursor.execute("INSERT INTO Attendance (EmployeeID, Date, ClockIn, Attendance) VALUES (%s, %s, %s, %s)", (employeeid, date_obj.strftime("%Y-%m-%d"), time_obj.strftime("%H:%M:%S"), 'On time'))

            # Commit changes to the database
            self.mydb.commit()
            return "Clock in successful."
        except mysql.connector.Error as error:
            print("Failed to execute query:", error)
            return "Failed Attendance Class"
        except ValueError as e:
            print("Error:", e)
            return "Failed Attendance Class"
        finally:
            self.mydb.close()
    def EmployeeClockOut(self, employeeid,timeout):
        time_obj = datetime.strptime(timeout, "%I:%M:%S %p")
        formatted_time = time_obj.strftime("%H:%M:%S")
        try:
            self.mycursor.execute("SELECT AttendanceID FROM Attendance WHERE EmployeeID = %s AND ClockOut IS NULL",(employeeid,))
            unclocked_entry = self.mycursor.fetchone()
            if unclocked_entry:
                attendance_id = unclocked_entry[0]
                self.mycursor.execute("UPDATE Attendance SET ClockOut = %s WHERE AttendanceID = %s",(formatted_time,attendance_id,))
                self.mydb.commit()
                print("Clock-out time updated successfully.")
            else:
                print("No unclocked entry found for the employee.")
        except mysql.connector.Error as error:
            print("Failed to update clock-out time:", error)
        finally:
            self.mydb.close()
    def EmployeeViewPastWorkHistory(self,employeeid):
        try:
            self.mycursor.execute("SELECT Date,ClockIn,ClockOut,Attendance FROM Attendance where employeeid = '{}';".format(employeeid))
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
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
        finally:
            self.mydb.close()

