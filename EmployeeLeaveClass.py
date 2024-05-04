import mysql.connector
import json
from datetime import datetime, timedelta
import NotificationClass

class EmployeeLeave:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host ='bdpspl67hpsxmkiiukdu-mysql.services.clever-cloud.com',
            user ='u5fgsonwyoke5bff',
            password='nHsZUdEJQ30AYtYXN6nF',
            database='bdpspl67hpsxmkiiukdu',
            port = '3306'
        )
        self.mycursor = self.mydb.cursor()
    def CreateEmployeeLeave(self, employeeId, date, leavetype):
        try:
            self.mycursor.execute("INSERT INTO  EmployeeLeave (employeeId, date, leavetype,status) VALUES ('{}','{}', '{}','Pending')".format(employeeId, date, leavetype))
            self.mydb.commit()
            if (leavetype == "emergency"):
                self.mycursor.execute("Select email from ManagerInCharge;")
                data = self.mycursor.fetchone()
                recipient_email = data[0]
                notification = NotificationClass.Notification()
                notification.send_email_to_manager(recipient_email,date)
            print("Success")
        except mysql.connector.Error as error:
            print("Failed EmployeeLeaveClass")
        finally:
            self.mydb.close()
    def EmployeeViewLeave(self):
        try:
            self.mycursor.execute("select * from EmployeeLeave;")
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
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
        finally:
            self.mydb.close()
    def EmployeeDeleteLeave(self, LeaveID):
        try:
            self.mycursor.execute("delete from EmployeeLeave where LeaveID = '{}'".format(LeaveID))
            self.mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
           print("Failed {}".format(error))
        finally:
            self.mydb.close()
    def EmployeeViewPendingLeave(self,employeeid):
        try:
            self.mycursor.execute("select leaveid, employeeid, date, leavetype from EmployeeLeave where status = 'Pending' and employeeid = '{}';".format(employeeid))
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = []
                for row in data:
                    leaveDate = row[2].strftime('%Y-%m-%d') if row[2] is not None else None
                    result.append((row[0], row[1], leaveDate, row[3]))
                print(json.dumps(result))
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            self.mydb.close()
    def ManagerViewPendingLeave(self):
        try:
            self.mycursor.execute("select leaveid, employeeid, date, leavetype from EmployeeLeave where status = 'Pending';")
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
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
        finally:
            self.mydb.close()
    def ManagerApproveLeave(self,id):
        try:
            self.mycursor.execute("SELECT leavetype from EmployeeLeave where leaveid = '{}'".format(id))
            leavetype = self.mycursor.fetchone()[0]
            self.mycursor.execute("SELECT employeeid from EmployeeLeave where leaveid = '{}'".format(id))
            employeeid = self.mycursor.fetchone()[0]
            self.mycursor.execute("update EmployeeLeave SET status = 'Approved' where leaveid = '{}'".format(id))
            self.mydb.commit()
            self.mycursor.execute("SELECT date from EmployeeLeave where leaveid = '{}'".format(id))
            date = self.mycursor.fetchone()[0]
            self.mycursor.execute("SELECT u.Email FROM EmployeeLeave el JOIN userAccount u ON el.EmployeeID = u.EmployeeID WHERE el.LeaveID = %s", (id,))
            employee_email = self.mycursor.fetchone()[0]
            status = 'Approved'
            notification = NotificationClass.Notification()
            notification.send_email_for_leave(employee_email, status, date)
            notif_message = f"Your Leave on {date} is Approved"
            self.mycursor.execute("INSERT into Notification (employeeid, notif) values ('{}','{}')".format(employeeid,notif_message))
            self.mydb.commit()
            self.mycursor.execute("INSERT into ApprovedEmployeeLeave (EmployeeID, Date, LeaveType, status) values ('{}','{}','{}','Approved')".format(employeeid,date,leavetype))
            self.mydb.commit()
            print("Success")
        except Exception as error:
            print(error)
        finally:
            self.mydb.close()
    def ManagerRejectLeave(self,id,reason):
        try:
            self.mycursor.execute("SELECT employeeid from EmployeeLeave where leaveid = '{}'".format(id))
            employeeid = self.mycursor.fetchone()[0]
            self.mycursor.execute("update EmployeeLeave SET status = 'Rejected', reason = '{}' where leaveid = '{}'".format(reason,id))
            self.mydb.commit()
            self.mycursor.execute("SELECT date from EmployeeLeave where leaveid = '{}'".format(id))
            date = self.mycursor.fetchone()[0]
            self.mycursor.execute("SELECT u.Email FROM EmployeeLeave el JOIN userAccount u ON el.EmployeeID = u.EmployeeID WHERE el.LeaveID = %s", (id,))
            employee_email = self.mycursor.fetchone()[0]
            status = 'Rejected'
            notification = NotificationClass.Notification()
            notification.send_email_for_leave(employee_email, status, date)
            notif_message = f"Your Leave on {date} is Rejected because {reason}"
            self.mycursor.execute("INSERT into Notification (employeeid, notif) values ('{}','{}')".format(employeeid,notif_message))
            self.mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            self.mydb.close()
    def ManagerViewApprovedLeave(self):
        try:
            self.mycursor.execute("select leaveid, employeeid, date, leavetype from EmployeeLeave where status = 'Approved';")
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No approved leave requests")
            else:
                result = []
                for row in data:
                    leaveDate = row[2].strftime('%Y-%m-%d') if row[2] is not None else None
                    result.append((row[0], row[1], leaveDate, row[3]))
                print(json.dumps(result))
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            self.mydb.close()
    def grableavecolumns(self):
        self.mycursor.execute("select column_name from information_schema.columns where table_schema = 'bdpspl67hpsxmkiiukdu' and table_name = 'EmployeeLeave' and column_name not in ('EmployeeID','LeaveID','reason','status')")
        data = self.mycursor.fetchall()
        result = json.dumps(data)
        self.mydb.close()
        print(result)
    def EmployeeUpdateLeave(self,leaveid,selectedoption,value):
        try:
            self.mycursor.execute("update EmployeeLeave SET {} = '{}' where leaveid = '{}'".format(selectedoption,value,leaveid))
            self.mydb.commit()
            if (value == "Emergency Leave"):
                self.mycursor.execute("select date from EmployeeLeave where leaveid = '{}'".format(leaveid))
                data = self.mycursor.fetchone()
                leavedate = data[0]
                self.mycursor.execute("Select email from ManagerInCharge;")
                data = self.mycursor.fetchone()
                recipient_email = data[0]
                notification = NotificationClass.Notification()
                notification.send_email_to_manager(recipient_email,leavedate)
            print("Success")
        except Exception as error:
            print(error)
        finally:
            self.mydb.close()
