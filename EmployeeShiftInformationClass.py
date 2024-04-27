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
            mycursor.execute("SELECT DISTINCT shiftpref FROM employeeshiftinformation;")
            shift_pref_data = mycursor.fetchall()
            shift_pref_count = mycursor.rowcount
            
            mycursor.execute("SELECT DISTINCT day FROM employeeshiftinformation;")
            day_data = mycursor.fetchall()
            day_count = mycursor.rowcount
            
            if shift_pref_count == 0 and day_count == 0:
                print("No data found")
            else:
                shift_pref_result = json.dumps(shift_pref_data)
                day_result = json.dumps(day_data)
                combined_result = {"shift_pref": shift_pref_result, "day": day_result}
                print(json.dumps(combined_result))
        except mysql.connector.Error as error:
            print("Failed")
    def FilterShiftPreference(self,day,shiftpref):
        try:
            mycursor.execute("select employeeid, fullname, shiftpref, mainrole,job from useraccount natural join employeeshiftinformation natural join userprofile where day = '{}' and shiftPref = '{}';".format(day,shiftpref))
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
            mycursor.execute("select employeeid, fullname, shiftpref,day, mainrole,job from useraccount natural join employeeshiftinformation natural join userprofile;")
            searchingdata = mycursor.fetchall()
            numberofrow = mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
    def ManagerCreateEmployeeShiftPreferece(self,schedule,employeeid):
        try:
            for day, shift in schedule.items():
                mycursor.execute("INSERT INTO EmployeeShiftInformation (EmployeeID, Day, ShiftPref, NoOfHrsWorked) VALUES ('{}', '{}','{}', '0')".format(employeeid,day,shift['shift']))
                mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
    def EmployeeUpdateShiftPreference(self,schedule,employeeid):
        try:
            mycursor.execute("select NoOfHrsWorked from EmployeeShiftInformation where EmployeeID = '{}'".format(employeeid))
            hours = mycursor.fetchall()
            print(hours[0][0])
            mycursor.execute("DELETE FROM EmployeeShiftInformation WHERE EmployeeID = %s", (employeeid,))
            mydb.commit()
            for day, shift in schedule.items():
                mycursor.execute("INSERT INTO EmployeeShiftInformation (EmployeeID, Day, ShiftPref, NoOfHrsWorked) VALUES ('{}', '{}','{}', '{}')".format(employeeid,day,shift['shift'],hours[0][0]))
                mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print(error)
    def ManagerUpdateHoursWorkedZero(self):
        try:
            mycursor.execute("Update EmployeeShiftInformation set NoOfHrsWorked = 0 where employeeid > 0;")
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")

    

        