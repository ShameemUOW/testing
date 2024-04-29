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

class Feedback:
    def __init__(self):
        pass
    def ViewFeedback(self):
        try:
            mycursor.execute("SELECT * FROM Feedback;")
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                print(json.dumps(data))
        except mysql.connector.Error as error:
            print ("Failed")
    def CreateFeedback(self,feedback):
        try:
            mycursor.execute("INSERT INTO Feedback (FeedbackInfo) VALUES ('{}')".format(feedback))
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print(error) 