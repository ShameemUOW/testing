import mysql.connector
import json

mydb = mysql.connector.connect(
    host ='bdpspl67hpsxmkiiukdu-mysql.services.clever-cloud.com',
    user ='u5fgsonwyoke5bff',
    password='nHsZUdEJQ30AYtYXN6nF',
    database='bdpspl67hpsxmkiiukdu',
    port = '3306'
)

mycursor = mydb.cursor()

class userProfile:
    def __init__(self):
        pass
    def userProfileSelect(self):
        try:
            mycursor.execute("select distinct mainrole From userProfile;")
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
    def createuserProfile(self,employeeid,selectedoption,role):
        try:
            mycursor.execute("INSERT INTO  userProfile VALUES ('{}','{}', '{}')".format(employeeid,selectedoption,role))
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed")
        finally:
            mydb.close()
    def updateuserProfile(self,employeeid,selectedoption,role):
        if (selectedoption == "Profile"):
            try:
                mycursor.execute("update userProfile SET mainrole = '{}' where employeeid = '{}'".format(role,employeeid))
                mydb.commit()
                mycursor.execute("update userAccount SET placeholder = '{}' where employeeid = '{}'".format(role,employeeid))
                mydb.commit()
                print("Success")
            except mysql.connector.Error as error:
                print("Failed")
            finally:
                mydb.close()
        elif (selectedoption == "Role"):
            try:
                mycursor.execute("update userProfile SET job = '{}' where employeeid = '{}'".format(role,employeeid))
                mydb.commit()
                print("Success")
            except mysql.connector.Error as error:
                print("Failed")
            finally:
                mydb.close()
    def AdminViewuserProfile(self):
        try:
            mycursor.execute("select employeeid, mainrole, job from userProfile;")
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


            

