import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()
mycursor.execute("use FYP;")


class WorkShift:
    def __init__(self):
        pass

    def createws(self, date, shift, start, end):
        try:
            sql = "INSERT INTO workshift (Date, shift, start, end) VALUES (%s, %s, %s, %s)"
            val = (date, shift, start, end)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Success")
        except mysql.connector.Error as error:
            print("Failed:", error)