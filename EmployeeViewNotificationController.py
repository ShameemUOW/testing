import NotificationClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
employeeid = x["employeeid"]

class EmployeeViewNotificationController:
    def EmployeeViewNotificationController(employeeid):
        evnc = NotificationClass.Notification()
        evnc.ViewNotifications(employeeid)

evnc = EmployeeViewNotificationController.EmployeeViewNotificationController(employeeid)