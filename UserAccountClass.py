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
