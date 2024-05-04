import mysql.connector
import json
from hashlib import sha256
from datetime import datetime

class UserAccount:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host ='bdpspl67hpsxmkiiukdu-mysql.services.clever-cloud.com',
            user ='u5fgsonwyoke5bff',
            password='nHsZUdEJQ30AYtYXN6nF',
            database='bdpspl67hpsxmkiiukdu',
            port = '3306'
        )
        self.mycursor = self.mydb.cursor()
    def Login(self,username,password,mainrole):
        self.mycursor.execute("select Username, pass, mainrole from userAccount natural join userProfile where username = '{}' and pass = sha2('{}', 0) and mainrole = '{}'".format(username,password, mainrole))
        data = self.mycursor.fetchall()
        numberofrow = self.mycursor.rowcount
        if(numberofrow==0):
            return False
        else:
            data2 = data[0]
            if username == data2[0] and sha256(password.encode('utf-8')).hexdigest() == data2[1] and data2[2] == mainrole:
                return True
            else:
                return False
    def getEmployeeID(self,username,password,mainrole):
        try:
            self.mycursor.execute("select employeeid from userAccount natural join userProfile where username = '{}' and pass = sha2('{}', 0) and mainrole = '{}'".format(username,password, mainrole))
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")
    def createAdminAccount(self, fullname, address, email, mobile, username,password,Chatid,MaxHours):
        try:
            self.mycursor.execute("INSERT INTO  userAccount (fullname, address, email, mobile, username,pass,MaxHours,Chatid,PlaceHolder) VALUES ('{}','{}', '{}','{}', '{}', '{}','{}','{}','Admin')".format(fullname, address, email, mobile, username,password,MaxHours,Chatid))
            self.mydb.commit()
            print("Success")
            self.HashPlainPasswords()
        except mysql.connector.Error as error:
            print("Failed")
    def createEmployeeAccount(self, fullname, address, email, mobile, username,password,Chatid, MaxHours):
        try:
            self.mycursor.execute("INSERT INTO  userAccount (fullname, address, email, mobile, username,pass,MaxHours,Chatid,PlaceHolder) VALUES ('{}','{}', '{}','{}', '{}', '{}','{}','{}','Employee')".format(fullname, address, email, mobile, username,password,MaxHours,Chatid))
            self.mydb.commit()
            print("Success")
            self.HashPlainPasswords()
        except mysql.connector.Error as error:
            print("Failed")
    def createManagerAccount(self, fullname, address, email, mobile, username,password,Chatid, MaxHours):
        try:
            self.mycursor.execute("INSERT INTO  userAccount (fullname, address, email, mobile, username,pass,MaxHours,Chatid,PlaceHolder) VALUES ('{}','{}', '{}','{}', '{}', '{}','{}','{}','Manager')".format(fullname, address, email, mobile, username,password,MaxHours,Chatid))
            self.mydb.commit()
            print("Success")
            self.HashPlainPasswords()
        except mysql.connector.Error as error:
            print("Failed")
    def AdminUpdateAdminAccount(self,employeeid,selectedoption,value):
        try:
            self.mycursor.execute("select mainrole from userProfile where employeeid = '{}'".format(employeeid))
            data = self.mycursor.fetchone()
            result = data[0]
            if (result == 'Admin'):
                try:
                    self.mycursor.execute("update userAccount SET {} = '{}' where employeeid = '{}'".format(selectedoption,value,employeeid))
                    self.mydb.commit()
                    print("Success")
                    self.HashPlainPasswords()
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
    def AdminUpdateManagerAccount(self,employeeid,selectedoption,value):
        try:
            self.mycursor.execute("select mainrole from userProfile where employeeid = '{}'".format(employeeid))
            data = self.mycursor.fetchone()
            result = data[0]
            if (result == 'Manager'):
                try:
                    self.mycursor.execute("update userAccount SET {} = '{}' where employeeid = '{}'".format(selectedoption,value,employeeid))
                    self.mydb.commit()
                    print("Success")
                    self.HashPlainPasswords()
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
    def AdminUpdateEmployeeAccount(self,employeeid,selectedoption,value):
        try:
            self.mycursor.execute("select mainrole from userProfile where employeeid = '{}'".format(employeeid))
            data = self.mycursor.fetchone()
            result = data[0]
            if (result == 'Employee'):
                try:
                    self.mycursor.execute("update userAccount SET {} = '{}' where employeeid = '{}'".format(selectedoption,value,employeeid))
                    self.mydb.commit()
                    print("Success")
                    self.HashPlainPasswords()
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
    def DeleteAdminAccount(self,employeeid):
        try:
            self.mycursor.execute("select mainrole from userProfile where employeeid = '{}'".format(employeeid))
            data = self.mycursor.fetchone()
            result = data[0]
            if (result == 'Admin'):
                try:
                    self.mycursor.execute("delete from userAccount where employeeid = '{}'".format(employeeid))
                    self.mydb.commit()
                    print("Success")
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
    def DeleteManagerAccount(self,employeeid):
        try:
            self.mycursor.execute("select mainrole from userProfile where employeeid = '{}'".format(employeeid))
            data = self.mycursor.fetchone()
            result = data[0]
            if (result == 'Manager'):
                try:
                    self.mycursor.execute("delete from userAccount where employeeid = '{}'".format(employeeid))
                    self.mydb.commit()
                    print("Success")
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
    def DeleteEmployeeAccount(self,employeeid):
        try:
            today = datetime.now().date()
            self.mycursor.execute("select * from EmployeeShift where employeeid = '{}' and shiftDate > '{}'".format(employeeid,today))
            shifts = self.mycursor.fetchall()
            if shifts:
                print("Reassign")
            else:
                self.mycursor.execute("select mainrole from userProfile where employeeid = '{}'".format(employeeid))
                data = self.mycursor.fetchone()
                result = data[0]
                if (result == 'Employee'):
                    try:
                        self.mycursor.execute("delete from userAccount where employeeid = '{}'".format(employeeid))
                        self.mydb.commit()
                        print("Success")
                    except mysql.connector.Error as error:
                        print("Failed")
                else:
                    print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
    def EmployeeViewAccount(self, employeeid):
        try:
            self.mycursor.execute("SELECT employeeid, Fullname, Address, Email, mobile, Username, maxhours FROM userAccount WHERE employeeid = '{}'".format(employeeid))
            data = self.mycursor.fetchone()
            if data is None:
                print("No data found for employee with ID:", employeeid)
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print("Failed to execute query:", error)

    def AdminViewAdminAccount(self):
        try:
            self.mycursor.execute("select employeeid, Fullname, Address,Email,mobile,Username,chatid,maxhours from userAccount where placeholder = 'Admin';")
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")
    def AdminViewManagerAccount(self):
        try:
            self.mycursor.execute("select employeeid, Fullname, Address,Email,mobile,Username,chatid,maxhours from userAccount where placeholder = 'Manager';")
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")
    def AdminViewEmployeeAccount(self):
        try:
            self.mycursor.execute("select employeeid, Fullname, Address,Email,mobile,Username,chatid,maxhours from userAccount where placeholder = 'Employee';")
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")
    def updateManagerAccount(self,employeeid,selectedoption,value):
        try:
            self.mycursor.execute("UPDATE userAccount SET {} = '{}' where employeeid = {}".format(selectedoption,value,employeeid))
            self.mydb.commit()
            print("Success")
            self.HashPlainPasswords()
        except mysql.connector.Error as error:
            print("Failed")
    def updateEmployeeAccount(self,employeeid,selectedoption,value):
        try:
            self.mycursor.execute("UPDATE userAccount SET {} = '{}' where employeeid = {}".format(selectedoption,value,employeeid))
            self.mydb.commit()
            print("Success")
            self.HashPlainPasswords()
        except mysql.connector.Error as error:
            print("Failed")
    def searchAdminAccount(self, selectedoption,value):
        try:
            self.mycursor.execute("select Fullname,Address,Email,Mobile,Username,pass,chatid,MaxHours from userAccount where {} = '{}' and placeholder = 'Admin'".format(selectedoption,value))
            searchingdata = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
    def filterAdminAccount(self, selectedoption,value):
        try:
            self.mycursor.execute("select EmployeeID,Fullname,Address,Email,Mobile,Username from userAccount where {} LIKE '%{}%' and placeholder = 'Admin'".format(selectedoption,value))
            searchingdata = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
    def searchManagerAccount(self, selectedoption,value):
        try:
            self.mycursor.execute("select EmployeeID,Fullname,Address,Email,Mobile,Username,pass,chatid,MaxHours from userAccount where {} = '{}' and placeholder = 'Manager'".format(selectedoption,value))
            searchingdata = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
    def filterManagerAccount(self, selectedoption,value):
        try:
            self.mycursor.execute("select EmployeeID,Fullname,Address,Email,Mobile,Username from userAccount where {} LIKE '%{}%' and placeholder = 'Manager'".format(selectedoption,value))
            searchingdata = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
    def searchEmployeeAccount(self, selectedoption,value):
        try:
            self.mycursor.execute("select EmployeeID,Fullname,Address,Email,Mobile,Username,pass,chatid,MaxHours from userAccount where {} = '{}' and placeholder = 'Employee'".format(selectedoption,value))
            searchingdata = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
    def filterEmployeeAccount(self, selectedoption,value):
        try:
            self.mycursor.execute("select EmployeeID,Fullname,Address,Email,Mobile,Username from userAccount where {} LIKE '%{}%' and placeholder = 'Employee'".format(selectedoption,value))
            searchingdata = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
    def grabUserAccountTableColumns(self):
        self.mycursor.execute("select column_name from information_schema.columns where table_schema = 'bdpspl67hpsxmkiiukdu' and table_name = 'userAccount' and column_name not in ('EmployeeID')")
        data = self.mycursor.fetchall()
        result = json.dumps(data)
        print(result)
    def grabFilterUserAccountTableColumns(self):
        self.mycursor.execute("select column_name from information_schema.columns where table_schema = 'bdpspl67hpsxmkiiukdu' and table_name = 'userAccount' and column_name not in ('pass','chatid','PlaceHolder','MaxHours')")
        data = self.mycursor.fetchall()
        result = json.dumps(data)
        print(result)
    def ManagerViewEmployeeAccount(self):
        try:
            self.mycursor.execute("select employeeid, Fullname, Address,Email,mobile,chatid,maxhours,job from userAccount natural join userProfile where mainrole = 'Employee';")
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")
    def ManagerFiltergrabTableColumns(self):
        self.mycursor.execute("select column_name from information_schema.columns where table_schema = 'bdpspl67hpsxmkiiukdu' and table_name = 'userAccount' and column_name not in ('PlaceHolder','Username','pass') union select column_name from information_schema.columns where table_schema = 'bdpspl67hpsxmkiiukdu' and table_name = 'userProfile' and column_name not in ('EmployeeID','MainRole') union select column_name from information_schema.columns where table_schema = 'bdpspl67hpsxmkiiukdu' and table_name = 'EmployeeShiftInformation' and column_name not in ('EmployeeID','ShiftPref');")
        data = self.mycursor.fetchall()
        result = json.dumps(data)
        print(result)
    def ManagerFilterEmployees(self, selectedoption,value):
        try:
            self.mycursor.execute("SELECT DISTINCT EmployeeID, FullName, Address, Email, Mobile, chatid, MaxHours, Job, NoOfHrsWorked FROM userAccount NATURAL JOIN EmployeeShiftInformation NATURAL JOIN userProfile WHERE {} LIKE '%{}%';'".format(selectedoption,value))
            searchingdata = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
    def ManagerSearchEmployees(self, selectedoption,value):
        try:
            self.mycursor.execute("select DISTINCT EmployeeID,FullName,Address,Email,Mobile,chatid,MaxHours,Job,NoOfHrsWorked from userAccount natural join EmployeeShiftInformation natural join userProfile where {} = '{}';'".format(selectedoption,value))
            searchingdata = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
    def HashPlainPasswords(self):
        try:
            self.mycursor.execute("update userAccount set userAccount.Pass = sha2(userAccount.Pass,0) where userAccount.EmployeeID > 0 AND char_length(userAccount.Pass) < 64")
            self.mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
    def ResetPassword(self, newpassword, employeeid):
        try:
            self.mycursor.execute("update userAccount set userAccount.Pass = sha2('{}',0) where userAccount.EmployeeID = {}".format(newpassword, employeeid))
            self.mydb.commit()
            self.HashPlainPasswords()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
    def SetManagerInCharge(self, employeeid):
        try:
            # Retrieve employee details
            self.mycursor.execute("SELECT employeeid, fullname, email FROM userAccount WHERE employeeid = %s", (employeeid,))
            employee_data = self.mycursor.fetchone()
            if employee_data:
                # Truncate the ManagerInCharge table
                self.mycursor.execute("TRUNCATE TABLE ManagerInCharge")

                # Insert employee details into ManagerInCharge table
                self.mycursor.execute("INSERT INTO ManagerInCharge (EmployeeID, Fullname, Email) VALUES (%s, %s, %s)", employee_data)
                self.mydb.commit()
                print("Success")
            else:
                print("Employee not found")
        except mysql.connector.Error as error:
            print("Failed")

