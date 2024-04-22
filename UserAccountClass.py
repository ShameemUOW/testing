import mysql.connector
import json
from hashlib import sha256
from datetime import datetime

mydb = mysql.connector.connect(
    host ='bdpspl67hpsxmkiiukdu-mysql.services.clever-cloud.com',
    user ='u5fgsonwyoke5bff',
    password='nHsZUdEJQ30AYtYXN6nF',
    database='bdpspl67hpsxmkiiukdu',
    port = '3306'
)
mycursor = mydb.cursor()

class userAccount:
    def __init__(self):
        pass
    def Login(self,username,password,mainrole):
        mycursor.execute("select Username, pass, mainrole from userAccount natural join userProfile where username = '{}' and pass = sha2('{}', 0) and mainrole = '{}'".format(username,password, mainrole))
        data = mycursor.fetchall()
        numberofrow = mycursor.rowcount
        if(numberofrow==0):
            mydb.close()
            return False
        else:
            data2 = data[0]
            if username == data2[0] and sha256(password.encode('utf-8')).hexdigest() == data2[1] and data2[2] == mainrole:
                mydb.close()
                return True
            else:
                mydb.close()
                return False
    def getEmployeeID(self,username,password,mainrole):
        try:
            mycursor.execute("select employeeid from userAccount natural join userProfile where username = '{}' and pass = sha2('{}', 0) and mainrole = '{}'".format(username,password, mainrole))
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            mydb.close()   
    def createAdminAccount(self, fullname, address, email, mobile, username,password,Chatid,MaxHours):
        try:
            mycursor.execute("INSERT INTO  userAccount (fullname, address, email, mobile, username,pass,MaxHours,Chatid,PlaceHolder) VALUES ('{}','{}', '{}','{}', '{}', '{}','{}','{}','Admin')".format(fullname, address, email, mobile, username,password,MaxHours,Chatid))
            mydb.commit()
            print("Success")
            self.HashPlainPasswords()
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            mydb.close()   
    def createEmployeeAccount(self, fullname, address, email, mobile, username,password,Chatid, MaxHours):
        try:
            mycursor.execute("INSERT INTO  userAccount (fullname, address, email, mobile, username,pass,MaxHours,Chatid,PlaceHolder) VALUES ('{}','{}', '{}','{}', '{}', '{}','{}','{}','Employee')".format(fullname, address, email, mobile, username,password,MaxHours,Chatid))
            mydb.commit()
            print("Success")
            self.HashPlainPasswords()
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            mydb.close()   
    def createManagerAccount(self, fullname, address, email, mobile, username,password,Chatid, MaxHours):
        try:
            mycursor.execute("INSERT INTO  userAccount (fullname, address, email, mobile, username,pass,MaxHours,Chatid,PlaceHolder) VALUES ('{}','{}', '{}','{}', '{}', '{}','{}','{}','Manager')".format(fullname, address, email, mobile, username,password,MaxHours,Chatid))
            mydb.commit()
            print("Success")
            self.HashPlainPasswords()
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            mydb.close()   
    def AdminUpdateAdminAccount(self,employeeid,selectedoption,value):
        try:
            mycursor.execute("select mainrole from userProfile where employeeid = '{}'".format(employeeid))
            data = mycursor.fetchone()
            result = data[0]
            if (result == 'Admin'):
                try:
                    mycursor.execute("update userAccount SET {} = '{}' where employeeid = '{}'".format(selectedoption,value,employeeid))
                    mydb.commit()
                    print("Success")
                    self.HashPlainPasswords()
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            mydb.close()   
    def AdminUpdateManagerAccount(self,employeeid,selectedoption,value):
        try:
            mycursor.execute("select mainrole from userProfile where employeeid = '{}'".format(employeeid))
            data = mycursor.fetchone()
            result = data[0]
            if (result == 'Manager'):
                try:
                    mycursor.execute("update userAccount SET {} = '{}' where employeeid = '{}'".format(selectedoption,value,employeeid))
                    mydb.commit()
                    print("Success")
                    self.HashPlainPasswords()
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            mydb.close()   
    def AdminUpdateEmployeeAccount(self,employeeid,selectedoption,value):
        try:
            mycursor.execute("select mainrole from userProfile where employeeid = '{}'".format(employeeid))
            data = mycursor.fetchone()
            result = data[0]
            if (result == 'Employee'):
                try:
                    mycursor.execute("update userAccount SET {} = '{}' where employeeid = '{}'".format(selectedoption,value,employeeid))
                    mydb.commit()
                    print("Success")
                    self.HashPlainPasswords()
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            mydb.close()   
    def DeleteAdminAccount(self,employeeid):
        try:
            mycursor.execute("select mainrole from userProfile where employeeid = '{}'".format(employeeid))
            data = mycursor.fetchone()
            result = data[0]
            if (result == 'Admin'):
                try:
                    mycursor.execute("delete from userAccount where employeeid = '{}'".format(employeeid))
                    mydb.commit()
                    print("Success")
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            mydb.close()   
    def DeleteManagerAccount(self,employeeid):
        try:
            mycursor.execute("select mainrole from userProfile where employeeid = '{}'".format(employeeid))
            data = mycursor.fetchone()
            result = data[0]
            if (result == 'Manager'):
                try:
                    mycursor.execute("delete from userAccount where employeeid = '{}'".format(employeeid))
                    mydb.commit()
                    print("Success")
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            mydb.close()   
    def DeleteEmployeeAccount(self,employeeid):
        try:
            today = datetime.now().date()
            mycursor.execute("select * from EmployeeShift where employeeid = '{}' and shiftDate > '{}'".format(employeeid,today))
            shifts = mycursor.fetchall()
            if shifts:
                print("Reassign")
            else:
                mycursor.execute("select mainrole from userProfile where employeeid = '{}'".format(employeeid))
                data = mycursor.fetchone()
                result = data[0]
                if (result == 'Employee'):
                    try:
                        mycursor.execute("delete from userAccount where employeeid = '{}'".format(employeeid))
                        mydb.commit()
                        print("Success")
                    except mysql.connector.Error as error:
                        print("Failed")
                else:
                    print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            mydb.close()   
    def EmployeeViewAccount(self, employeeid):
        try:
            mycursor.execute("SELECT employeeid, Fullname, Address, Email, mobile, Username, maxhours FROM userAccount WHERE employeeid = '{}'".format(employeeid))
            data = mycursor.fetchone()
            if data is None:
                print("No data found for employee with ID:", employeeid)
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print("Failed to execute query:", error)
        finally:
            mydb.close()   
    def AdminViewAdminAccount(self):
        try:
            mycursor.execute("select employeeid, Fullname, Address,Email,mobile,Username,chatid,maxhours from userAccount where placeholder = 'Admin';")
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            mydb.close()   
    def AdminViewManagerAccount(self):
        try:
            mycursor.execute("select employeeid, Fullname, Address,Email,mobile,Username,chatid,maxhours from userAccount where placeholder = 'Manager';")
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            mydb.close()   
    def AdminViewEmployeeAccount(self):
        try:
            mycursor.execute("select employeeid, Fullname, Address,Email,mobile,Username,chatid,maxhours from userAccount where placeholder = 'Employee';")
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            mydb.close()   
    def updateManagerAccount(self,employeeid,selectedoption,value):
        try:
            mycursor.execute("UPDATE userAccount SET {} = '{}' where employeeid = {}".format(selectedoption,value,employeeid))
            mydb.commit()
            print("Success")
            self.HashPlainPasswords()
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            mydb.close()   
    def updateEmployeeAccount(self,employeeid,selectedoption,value):
        try:
            mycursor.execute("UPDATE userAccount SET {} = '{}' where employeeid = {}".format(selectedoption,value,employeeid))
            mydb.commit()
            print("Success")
            self.HashPlainPasswords()
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            mydb.close()   
    def searchAdminAccount(self, selectedoption,value):
        try:
            mycursor.execute("select Fullname,Address,Email,Mobile,Username,pass,chatid,MaxHours from userAccount where {} = '{}' and placeholder = 'Admin'".format(selectedoption,value))
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            mydb.close()   
    def filterAdminAccount(self, selectedoption,value):
        try:
            mycursor.execute("select EmployeeID,Fullname,Address,Email,Mobile,Username from userAccount where {} LIKE '%{}%' and placeholder = 'Admin'".format(selectedoption,value))
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            mydb.close()   
    def searchManagerAccount(self, selectedoption,value):
        try:
            mycursor.execute("select EmployeeID,Fullname,Address,Email,Mobile,Username,pass,chatid,MaxHours from userAccount where {} = '{}' and placeholder = 'Manager'".format(selectedoption,value))
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            mydb.close()   
    def filterManagerAccount(self, selectedoption,value):
        try:
            mycursor.execute("select EmployeeID,Fullname,Address,Email,Mobile,Username from userAccount where {} LIKE '%{}%' and placeholder = 'Manager'".format(selectedoption,value))
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            mydb.close()   
    def searchEmployeeAccount(self, selectedoption,value):
        try:
            mycursor.execute("select EmployeeID,Fullname,Address,Email,Mobile,Username,pass,chatid,MaxHours from userAccount where {} = '{}' and placeholder = 'Employee'".format(selectedoption,value))
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            mydb.close()   
    def filterEmployeeAccount(self, selectedoption,value):
        try:
            mycursor.execute("select EmployeeID,Fullname,Address,Email,Mobile,Username from userAccount where {} LIKE '%{}%' and placeholder = 'Employee'".format(selectedoption,value))
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            mydb.close()   
    def grabuserAccountTableColumns(self):
        mycursor.execute("select column_name from information_schema.columns where table_schema = 'bdpspl67hpsxmkiiukdu' and table_name = 'userAccount' and column_name not in ('EmployeeID')")
        data = mycursor.fetchall()
        result = json.dumps(data)
        mydb.close()
        print(result)
    def grabFilteruserAccountTableColumns(self):
        mycursor.execute("select column_name from information_schema.columns where table_schema = 'bdpspl67hpsxmkiiukdu' and table_name = 'userAccount' and column_name not in ('pass','chatid','PlaceHolder','MaxHours')")
        data = mycursor.fetchall()
        result = json.dumps(data)
        mydb.close()
        print(result)
    def ManagerViewEmployeeAccount(self):
        try:
            mycursor.execute("select employeeid, Fullname, Address,Email,mobile,chatid,maxhours,job from userAccount natural join userProfile where mainrole = 'Employee';")
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            mydb.close()   
    def ManagerFiltergrabTableColumns(self):
        mycursor.execute("select column_name from information_schema.columns where table_schema = 'bdpspl67hpsxmkiiukdu' and table_name = 'userAccount' and column_name not in ('PlaceHolder','Username','pass') union select column_name from information_schema.columns where table_schema = 'FYP' and table_name = 'userProfile' and column_name not in ('EmployeeID','MainRole') union select column_name from information_schema.columns where table_schema = 'FYP' and table_name = 'EmployeeShiftInformation' and column_name not in ('EmployeeID');")
        data = mycursor.fetchall()
        result = json.dumps(data)
        mydb.close()
        print(result)
    def ManagerFilterEmployees(self, selectedoption,value):
        try:
            mycursor.execute("select EmployeeID,FullName,Address,Email,Mobile,chatid,MaxHours,Job,ShiftPref,NoOfHrsWorked from userAccount natural join EmployeeShiftInformation natural join userProfile where {} LIKE '%{}%';'".format(selectedoption,value))
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            mydb.close()   
    def ManagerSearchEmployees(self, selectedoption,value):
        try:
            mycursor.execute("select EmployeeID,FullName,Address,Email,Mobile,chatid,MaxHours,Job,ShiftPref,NoOfHrsWorked from userAccount natural join EmployeeShiftInformation natural join userProfile where {} = '{}';'".format(selectedoption,value))
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            mydb.close()   
    def HashPlainPasswords(self):
        try:
            mycursor.execute("update userAccount set userAccount.Pass = sha2(userAccount.Pass,0) where userAccount.EmployeeID > 0 AND char_length(userAccount.Pass) < 64")
            mydb.commit()
            self.HashPlainPasswords()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            mydb.close()   
    def ResetPassword(self, newpassword, employeeid):
        try:
            mycursor.execute("update userAccount set userAccount.Pass = sha2('{}',0) where userAccount.EmployeeID = {}".format(newpassword, employeeid))
            mydb.commit()
            self.HashPlainPasswords()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            mydb.close()   

