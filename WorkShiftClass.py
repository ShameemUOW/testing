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
    def CreateMultipleWorkshifts(self, start_date_str, end_date_str, shift, start, end):
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
            # Generate a list of dates between start_date and end_date
            dates = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
            
            # Insert each date along with shift, start, and end into the database
            for date in dates:
                mycursor.execute("INSERT INTO workshift (date, shift, start, end) VALUES (%s, %s, %s, %s)", (date.strftime("%Y-%m-%d"), shift, start, end))
            
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
    def ManagerDeleteWorkShifts(self, id):
        try:
            mycursor.execute("delete from workshift where id = '{}'".format(id))
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
           print("Failed {}".format(error))
    def grabWorkShiftTableColumn(self):
        mycursor.execute("select column_name from information_schema.columns where table_schema = 'FYP' and table_name = 'workshift'")
        data = mycursor.fetchall()
        result = json.dumps(data)
        print(result)
    def ManagerFilterWorkShift(self, selectedoption,value):
        try:
            mycursor.execute("select * from workshift where {} LIKE '%{}%';".format(selectedoption,value))
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

    def updateWorkShift(self, id, selectedoption, value):
        try:
            mycursor.execute("update workshift set {} = '{}' where id = '{}'".format(selectedoption,value,id))
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")