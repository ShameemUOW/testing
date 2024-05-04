import mysql.connector
import json

class UserProfile:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host ='bdpspl67hpsxmkiiukdu-mysql.services.clever-cloud.com',
            user ='u5fgsonwyoke5bff',
            password='nHsZUdEJQ30AYtYXN6nF',
            database='bdpspl67hpsxmkiiukdu',
            port = '3306'
        )
        self.mycursor = self.mydb.cursor()
    def UserProfileSelect(self):
        try:
            self.mycursor.execute("select distinct mainrole From userProfile;")
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
    def createUserProfile(self,employeeid,selectedoption,role):
        try:
            self.mycursor.execute("INSERT INTO  userProfile VALUES ('{}','{}', '{}')".format(employeeid,selectedoption,role))
            self.mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            self.mydb.close()
    def updateUserProfile(self,employeeid,selectedoption,role):
        if (selectedoption == "Profile"):
            try:
                self.mycursor.execute("update userProfile SET mainrole = '{}' where employeeid = '{}'".format(role,employeeid))
                self.mydb.commit()
                self.mycursor.execute("update userAccount SET placeholder = '{}' where employeeid = '{}'".format(role,employeeid))
                self.mydb.commit()
                print("Success")
            except mysql.connector.Error as error:
                print("Failed")
            finally:
                self.mydb.close()
        elif (selectedoption == "Role"):
            try:
                self.mycursor.execute("update userProfile SET job = '{}' where employeeid = '{}'".format(role,employeeid))
                self.mydb.commit()
                print("Success")
            except mysql.connector.Error as error:
                print("Failed")
            finally:
                self.mydb.close()
    def AdminViewUserProfile(self):
        try:
            self.mycursor.execute("select employeeid, mainrole, job from userProfile;")
            data = self.mycursor.fetchall()
            numberofrow = self.mycursor.rowcount
            if(numberofrow==0):
                print("No table left")
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print ("Failed")
        finally:
            self.mydb.close()


            

