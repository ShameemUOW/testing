import mysql.connector
import json

class EmployeeShiftInformation:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host ='bdpspl67hpsxmkiiukdu-mysql.services.clever-cloud.com',
            user ='u5fgsonwyoke5bff',
            password='nHsZUdEJQ30AYtYXN6nF',
            database='bdpspl67hpsxmkiiukdu',
            port = '3306'
        )
        self.mycursor = self.mydb.cursor()
    def grabShiftTypes(self):
        try:
            self.mycursor.execute("SELECT DISTINCT shift FROM workshift;")
            shift_pref_data = self.mycursor.fetchall()
            shift_pref_count = self.mycursor.rowcount
            
            self.mycursor.execute("SELECT DISTINCT day FROM EmployeeShiftInformation;")
            day_data = self.mycursor.fetchall()
            day_count = self.mycursor.rowcount
            
            if shift_pref_count == 0 and day_count == 0:
                print("No data found")
            else:
                shift_pref_result = json.dumps(shift_pref_data)
                day_result = json.dumps(day_data)
                combined_result = {"shift_pref": shift_pref_result, "day": day_result}
                print(json.dumps(combined_result))
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            self.mydb.close()
    def FilterShiftPreference(self,day,shiftpref):
        try:
            self.mycursor.execute("select employeeid, fullname, shiftpref, mainrole,job from userAccount natural join EmployeeShiftInformation natural join userProfile where day = '{}' and shiftPref = '{}';".format(day,shiftpref))
            searchingdata = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            self.mydb.close()
    def ViewShiftPreference(self):
        try:
            self.mycursor.execute("select employeeid, fullname, shiftpref,day, mainrole,job from userAccount natural join EmployeeShiftInformation natural join userProfile;")
            searchingdata = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                searchingresult = json.dumps(searchingdata)
                print(searchingresult)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            self.mydb.close()
    def ManagerCreateEmployeeShiftPreferece(self,schedule,employeeid):
        try:
            for day, shift in schedule.items():
                self.mycursor.execute("INSERT INTO EmployeeShiftInformation (EmployeeID, Day, ShiftPref, NoOfHrsWorked) VALUES ('{}', '{}','{}', '0')".format(employeeid,day,shift['shift']))
                self.mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            self.mydb.close()
    def EmployeeUpdateShiftPreference(self,schedule,employeeid):
        try:
            self.mycursor.execute("select NoOfHrsWorked from EmployeeShiftInformation where EmployeeID = '{}'".format(employeeid))
            hours = self.mycursor.fetchall()
            print(hours[0][0])
            self.mycursor.execute("DELETE FROM EmployeeShiftInformation WHERE EmployeeID = %s", (employeeid,))
            self.mydb.commit()
            for day, shift in schedule.items():
                self.mycursor.execute("INSERT INTO EmployeeShiftInformation (EmployeeID, Day, ShiftPref, NoOfHrsWorked) VALUES ('{}', '{}','{}', '{}')".format(employeeid,day,shift['shift'],hours[0][0]))
                self.mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print(error)
        finally:
            self.mydb.close()
    def ManagerUpdateHoursWorkedZero(self):
        try:
            self.mycursor.execute("Update EmployeeShiftInformation set NoOfHrsWorked = 0 where employeeid > 0;")
            self.mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            self.mydb.close()

    

        