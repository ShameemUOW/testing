import mysql.connector
import json

mydb = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password='root',
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()
mycursor.execute("use FYP;")

class UserAccount:
    def __init__(self):
        pass
    def Login(self,username,password,mainrole):
        mycursor.execute("select Username, pass, mainrole from useraccount natural join userprofile where username = '{}' and pass = '{}' and mainrole = '{}'".format(username,password, mainrole))
        data = mycursor.fetchall()
        numberofrow = mycursor.rowcount
        if(numberofrow==0):
            return False
        else:
            data2 = data[0]
            if username == data2[0] and password == data2[1] and data2[2] == mainrole:
                return True
            else:
                return False
    def getEmployeeID(self,username,password,mainrole):
        try:
            mycursor.execute("select employeeid from useraccount natural join userprofile where username = '{}' and pass = '{}' and mainrole = '{}'".format(username,password, mainrole))
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")
    def createAdminAccount(self, fullname, address, email, mobile, username,password, MaxHours):
        try:
            mycursor.execute("INSERT INTO  useraccount (fullname, address, email, mobile, username,pass,MaxHours,PlaceHolder) VALUES ('{}','{}', '{}','{}', '{}', '{}','{}','Admin')".format(fullname, address, email, mobile, username,password,MaxHours))
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
    def createEmployeeAccount(self, fullname, address, email, mobile, username,password, MaxHours):
        try:
            mycursor.execute("INSERT INTO  useraccount (fullname, address, email, mobile, username,pass,MaxHours,PlaceHolder) VALUES ('{}','{}', '{}','{}', '{}', '{}','{}','Employee')".format(fullname, address, email, mobile, username,password,MaxHours))
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
    def createManagerAccount(self, fullname, address, email, mobile, username,password, MaxHours):
        try:
            mycursor.execute("INSERT INTO  useraccount (fullname, address, email, mobile, username,pass,MaxHours,PlaceHolder) VALUES ('{}','{}', '{}','{}', '{}', '{}','{}','Manager')".format(fullname, address, email, mobile, username,password,MaxHours))
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
    def AdminUpdateAdminAccount(self,employeeid,selectedoption,value):
        try:
            mycursor.execute("select mainrole from userprofile where employeeid = '{}'".format(employeeid))
            data = mycursor.fetchone()
            result = data[0]
            if (result == 'Admin'):
                try:
                    mycursor.execute("update useraccount SET {} = '{}' where employeeid = '{}'".format(selectedoption,value,employeeid))
                    mydb.commit()
                    print("Success")
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
    def AdminUpdateManagerAccount(self,employeeid,selectedoption,value):
        try:
            mycursor.execute("select mainrole from userprofile where employeeid = '{}'".format(employeeid))
            data = mycursor.fetchone()
            result = data[0]
            if (result == 'Manager'):
                try:
                    mycursor.execute("update useraccount SET {} = '{}' where employeeid = '{}'".format(selectedoption,value,employeeid))
                    mydb.commit()
                    print("Success")
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
    def AdminUpdateEmployeeAccount(self,employeeid,selectedoption,value):
        try:
            mycursor.execute("select mainrole from userprofile where employeeid = '{}'".format(employeeid))
            data = mycursor.fetchone()
            result = data[0]
            if (result == 'Employee'):
                try:
                    mycursor.execute("update useraccount SET {} = '{}' where employeeid = '{}'".format(selectedoption,value,employeeid))
                    mydb.commit()
                    print("Success")
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
    def DeleteAdminAccount(self,employeeid):
        try:
            mycursor.execute("select mainrole from userprofile where employeeid = '{}'".format(employeeid))
            data = mycursor.fetchone()
            result = data[0]
            if (result == 'Admin'):
                try:
                    mycursor.execute("delete from useraccount where employeeid = '{}'".format(employeeid))
                    mydb.commit()
                    print("Success")
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
    def DeleteManagerAccount(self,employeeid):
        try:
            mycursor.execute("select mainrole from userprofile where employeeid = '{}'".format(employeeid))
            data = mycursor.fetchone()
            result = data[0]
            if (result == 'Manager'):
                try:
                    mycursor.execute("delete from useraccount where employeeid = '{}'".format(employeeid))
                    mydb.commit()
                    print("Success")
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
    def DeleteEmployeeAccount(self,employeeid):
        try:
            mycursor.execute("select mainrole from userprofile where employeeid = '{}'".format(employeeid))
            data = mycursor.fetchone()
            result = data[0]
            if (result == 'Employee'):
                try:
                    mycursor.execute("delete from useraccount where employeeid = '{}'".format(employeeid))
                    mydb.commit()
                    print("Success")
                except mysql.connector.Error as error:
                    print("Failed")
            else:
                print("Failed")
        except mysql.connector.Error as error:
            print("Failed")
    def AdminViewAdminAccount(self):
        try:
            mycursor.execute("select employeeid, Fullname, Address,Email,mobile,Username,maxhours from useraccount where placeholder = 'Admin';")
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")
    def AdminViewManagerAccount(self):
        try:
            mycursor.execute("select employeeid, Fullname, Address,Email,mobile,Username,maxhours from useraccount where placeholder = 'Manager';")
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")
    def AdminViewEmployeeAccount(self):
        try:
            mycursor.execute("select employeeid, Fullname, Address,Email,mobile,Username,maxhours from useraccount where placeholder = 'Employee';")
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")
    def updateManagerAccount(self, fullname, email, password, mobile, username):
        try:
            mycursor.execute("UPDATE useraccount SET fullname = '{}', email = '{}', pass = '{}', mobile = '{}' WHERE username = '{}'".format(fullname,email,password,mobile,username))
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
    def searchAdminAccount(self, selectedoption,value):
        try:
            mycursor.execute("select Fullname,Address,Email,Mobile,Username,pass,MaxHours from useraccount where {} = '{}' and placeholder = 'Admin'".format(selectedoption,value))
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
    def searchManagerAccount(self, selectedoption,value):
        try:
            mycursor.execute("select Fullname,Address,Email,Mobile,Username,pass,MaxHours from useraccount where {} = '{}' and placeholder = 'Manager'".format(selectedoption,value))
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
    def searchEmployeeAccount(self, selectedoption,value):
        try:
            mycursor.execute("select Fullname,Address,Email,Mobile,Username,pass,MaxHours from useraccount where {} = '{}' and placeholder = 'Employee'".format(selectedoption,value))
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
    def grabUserAccountTableColumns(self):
        mycursor.execute("select column_name from information_schema.columns where table_schema = 'FYP' and table_name = 'useraccount' and column_name not in ('EmployeeID')")
        data = mycursor.fetchall()
        result = json.dumps(data)
        print(result)

