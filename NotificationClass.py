import mysql.connector
import json
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()
mycursor.execute("use FYP;")

class Notification:
    def __init__(self):
        pass
    def ViewNotifications(self, employeeid):
        try:
            mycursor.execute("SELECT * FROM notification WHERE employeeid = '{}'".format(employeeid))
            data = mycursor.fetchall()
            if data is None:
                print("No data found for employee with ID:", employeeid)
            else:
                result = json.dumps(data)
                print(result)
        except mysql.connector.Error as error:
            print("Failed to execute query:", error)
    def send_email(self,sender_email, sender_password, recipient_email, subject, message):
        # Set up the SMTP server
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_name = sender_email.split('@')[0]

        # Create a MIME multipart message
        msg = MIMEMultipart()
        msg['From'] = f"{sender_name} <{sender_email}>"
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the message
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Close the connection
        server.quit()
    def send_email_for_leave(self,recipient_email, status,date):
        sender_email = "simfypesr@gmail.com"
        sender_password = "dxfs lctf qgge hljc"
        subject = "Leave Outcome"
        message = f"Your Leave on {date} is {status}"

        self.send_email(sender_email, sender_password, recipient_email, subject, message)
    def send_email_for_ws(self,recipient_email, shifttype,date):
        sender_email = "simfypesr@gmail.com"
        sender_password = "dxfs lctf qgge hljc"
        subject = "You have been selected for a shift"
        message = f"Your new shift is on {date}, {shifttype}"

        self.send_email(sender_email, sender_password, recipient_email, subject, message)

