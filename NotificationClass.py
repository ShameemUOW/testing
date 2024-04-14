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

class Notification:
    def __init__(self):
        pass
    def ViewNotifications(self, employeeid):
        try:
            mycursor.execute("SELECT * FROM notification WHERE employeeid = '{}'".format(employeeid))
            data = mycursor.fetchall()
            if data is None:
                print("No data found for employee with ID:", employeeid)
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print("Failed to execute query:", error)
        
