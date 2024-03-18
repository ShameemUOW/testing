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

class EmployeeLeave:
    def __init__(self):
        pass
    def CreateEmployeeLeave(self, employeeId, date, leavetype):
        try:
            mycursor.execute("INSERT INTO  employeeleave (employeeId, date, leavetype,status) VALUES ('{}','{}', '{}','Pending')".format(employeeId, date, leavetype))
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed EmployeeLeaveClass")
    def EmployeeViewLeave(self):
        try:
            mycursor.execute("select * from employeeleave;")
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = []
                for row in data:
                    leaveDate = datetime.strptime(str(row[3]), '%H:%M:%S').time().strftime('%H:%M:%S') if row[3] is not None else None
                    result.append((row[0], row[1], row[2], leaveDate, row[4]))
                print(json.dumps(result))
        except mysql.connector.Error as error:
            print ("Failed")
    def EmployeeDeleteLeave(self, LeaveID):
        try:
            mycursor.execute("delete from employeeleave where LeaveID = '{}'".format(LeaveID))
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
           print("Failed {}".format(error))
    def ManagerViewPendingLeave(self):
        try:
            mycursor.execute("select leaveid, employeeid, date, leavetype from employeeleave where status = 'Pending';")
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No pending leave requests")
            else:
                result = []
                for row in data:
                    leaveDate = row[2].strftime('%Y-%m-%d') if row[2] is not None else None
                    result.append((row[0], row[1], leaveDate, row[3]))
                print(json.dumps(result))
        except mysql.connector.Error as error:
            print ("Failed")
    def ManagerApproveLeave(self,id):
        try:
            mycursor.execute("update employeeleave SET status = 'Approved' where leaveid = '{}'".format(id))
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
