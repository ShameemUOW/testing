import FeedbackClass
import sys
import json

input = sys.argv[1]
x=json.loads(input)
feedback = x["feedback"]

class CreateFeedbackController:
    def CreateFeedbackController(feedback):
        createfeedback = FeedbackClass.Feedback()
        createfeedback.CreateFeedback(feedback)

createfeedback = CreateFeedbackController.CreateFeedbackController(feedback)