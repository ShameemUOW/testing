import FeedbackClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
feedback = x["feedback"]

class EmployeeCreateFeedbackController:
    def EmployeeCreateFeedbackController(feedback):
        createfeedback = FeedbackClass.Feedback()
        createfeedback.EmployeeCreateFeedback(feedback)

createfeedback = EmployeeCreateFeedbackController.EmployeeCreateFeedbackController(feedback)