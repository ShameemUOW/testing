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

class UserProfile:
    def __init__(self):
        pass
    def UserProfileSelect(self):
        try:
            mycursor.execute("select distinct mainrole From userprofile;")
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
    def createUserProfile(self,employeeid,selectedoption,role):
        try:
            mycursor.execute("INSERT INTO  userprofile VALUES ('{}','{}', '{}')".format(employeeid,selectedoption,role))
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
    def updateUserProfile(self,employeeid,selectedoption,role):
        if (selectedoption == "Profile"):
            try:
                mycursor.execute("update userprofile SET mainrole = '{}' where employeeid = '{}'".format(role,employeeid))
                mydb.commit()
                mycursor.execute("update useraccount SET placeholder = '{}' where employeeid = '{}'".format(role,employeeid))
                mydb.commit()
                print("Success")
            except mysql.connector.Error as error:
                print("Failed")
        elif (selectedoption == "Role"):
            try:
                mycursor.execute("update userprofile SET job = '{}' where employeeid = '{}'".format(role,employeeid))
                mydb.commit()
                print("Success")
            except mysql.connector.Error as error:
                print("Failed")
    def AdminViewUserProfile(self):
        try:
            mycursor.execute("select employeeid, mainrole, job from userprofile;")
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")


            

