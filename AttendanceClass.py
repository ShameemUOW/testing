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
        
        