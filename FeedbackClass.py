import mysql.connector
import json
from datetime import datetime, timedelta

class Feedback:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host ='bdpspl67hpsxmkiiukdu-mysql.services.clever-cloud.com',
            user ='u5fgsonwyoke5bff',
            password='nHsZUdEJQ30AYtYXN6nF',
            database='bdpspl67hpsxmkiiukdu',
            port = '3306'
        )
        self.mycursor = self.mydb.cursor()
    def AdminViewFeedback(self):
        try:
            self.mycursor.execute("SELECT * FROM Feedback;")
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                print(json.dumps(data))
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            self.mydb.close()
    def ManagerViewFeedback(self):
        try:
            self.mycursor.execute("SELECT * FROM Feedback;")
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                print(json.dumps(data))
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            self.mydb.close()
    def ManagerCreateFeedback(self,feedback):
        try:
            self.mycursor.execute("INSERT INTO Feedback (FeedbackInfo) VALUES ('{}')".format(feedback))
            self.mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print(error) 
        finally:
            self.mydb.close()
    def EmployeeCreateFeedback(self,feedback):
        try:
            self.mycursor.execute("INSERT INTO Feedback (FeedbackInfo) VALUES ('{}')".format(feedback))
            self.mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print(error) 
        finally:
            self.mydb.close()