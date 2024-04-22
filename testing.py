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
            mycursor.execute("select w.date, a.cafeid, a.fullname, p.mainrole,p.job, a.mobile from userAccount a, userProfile p, workslots w where a.cafeid = p.cafeid and a.cafeid = w.cafeid;")
            data = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")

GetAll()