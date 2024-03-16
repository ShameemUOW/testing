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

class WorkShift:
    def __init__(self):
        pass
    def createws(self, date, shift, start, end):
        try:
            mycursor.execute("INSERT INTO  workshift (date, shift, start, end) VALUES ('{}','{}', '{}','{}')".format(date, shift, start, end))
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
    def ManagerViewWorkShifts(self):
        try:
            mycursor.execute("select * from workshift;")
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = []
                for row in data:
                    start_time = datetime.strptime(str(row[3]), '%H:%M:%S').time().strftime('%H:%M:%S') if row[3] is not None else None
                    end_time = datetime.strptime(str(row[4]), '%H:%M:%S').time().strftime('%H:%M:%S') if row[4] is not None else None
                    result.append((row[0], row[1], row[2], start_time, end_time))
                print(json.dumps(result))
        except mysql.connector.Error as error:
            print ("Failed")