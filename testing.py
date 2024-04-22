import mysql.connector
import json

mydb = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password='root',
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()
mycursor.execute("use cafe22;")

def GetAll():
        try:
            mycursor.execute("UPDATE userAccount SET {} = '{}' where employeeid = {}".format(selectedoption,value,employeeid))
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")

GetAll()