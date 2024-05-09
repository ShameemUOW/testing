import FeedbackClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
feedback = x["feedback"]

class ManagerCreateFeedbackController:
    def ManagerCreateFeedbackController(feedback):
        createfeedback = FeedbackClass.Feedback()
        createfeedback.ManagerCreateFeedback(feedback)

createfeedback = ManagerCreateFeedbackController.ManagerCreateFeedbackController(feedback)