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

class EmployeeShiftInformation:
    def __init__(self):
        pass
    def grabShiftTypes(self):
        try:
            mycursor.execute("select distinct shiftpref From employeeshiftinformation;")
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
    def FilterShiftPreference(self,selectedoption):
        try:
            mycursor.execute("select employeeid, fullname, shiftpref, mainrole,job from useraccount natural join employeeshiftinformation natural join userprofile where shiftPref = '{}';".format(selectedoption))
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
    def ViewShiftPreference(self):
        try:
            mycursor.execute("select employeeid, fullname, shiftpref, mainrole,job from useraccount natural join employeeshiftinformation natural join userprofile;")
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")

        