import mysql.connector
import json
from datetime import datetime, timedelta

class WorkShift:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host ='bdpspl67hpsxmkiiukdu-mysql.services.clever-cloud.com',
            user ='u5fgsonwyoke5bff',
            password='nHsZUdEJQ30AYtYXN6nF',
            database='bdpspl67hpsxmkiiukdu',
            port = '3306'
        )
        self.mycursor = self.mydb.cursor()
    def createws(self, date, shift, start, end):
        try:
            self.mycursor.execute("INSERT INTO  workshift (date, shift, start, end) VALUES ('{}','{}', '{}','{}')".format(date, shift, start, end))
            self.mydb.commit()
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
                self.mycursor.execute("INSERT INTO workshift (date, shift, start, end) VALUES (%s, %s, %s, %s)", (date.strftime("%Y-%m-%d"), shift, start, end))
            
            self.mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
    def ManagerViewWorkShifts(self):
        try:
            self.mycursor.execute("select * from workshift;")
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
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
            self.mycursor.execute("delete from workshift where id = '{}'".format(id))
            self.mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
           print("Failed {}".format(error))
    def grabWorkShiftTableColumn(self):
        self.mycursor.execute("select column_name from information_schema.columns where table_schema = 'bdpspl67hpsxmkiiukdu' and table_name = 'workshift'")
        data = self.mycursor.fetchall()
        result = json.dumps(data)
        print(result)
    def ManagerFilterWorkShift(self, selectedoption,value):
        try:
            self.mycursor.execute("select * from workshift where {} LIKE '%{}%';".format(selectedoption,value))
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
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
            self.mycursor.execute("update workshift set {} = '{}' where id = '{}'".format(selectedoption,value,id))
            self.mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")