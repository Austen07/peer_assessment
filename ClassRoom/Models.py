from keyConstants import *
from service import getClassRoomService
from collections import OrderedDict
from PeerReview.Logger import getLogger
from sheetUtility import readAssignmentDetails
from instructorUtility import getGradeFormsFolderId
from OAuth.views import get_global_account_credentials
import json

log = getLogger("Models")


def formatAssignmentDetails(credentials, request, courseId):
    form_details = OrderedDict()
    for k in INSTRUCTOR_FORM_KEYS:
        if k in request.keys():
            form_details[k] = request[k]
        else:
            form_details[k] = ""
    number_questions = int(form_details['numberQuestions'])
    for i in range(1, number_questions + 1):
        form_details["q-" + str(i)] = request["q-" + str(i)]
    return form_details


def formatGradeDetails(req, count):
    form_details = {}
    for k in GRADE_FORM_KEYS:
        a = []
        for i in range(0, int(count)):
            key = k + str(i + 1)
            a.append(req[key] if key in req.keys() else "")
        form_details[k] = a
    return form_details


def getAssignmentDetails(courseId, assId):
    globalAccountCredentials = get_global_account_credentials()
    driveResourceLinkId = getGradeFormsFolderId(globalAccountCredentials, courseId)
    a = readAssignmentDetails(globalAccountCredentials, driveResourceLinkId, courseId, assId)
    return a


def updateGradingData(details, oldDetails, assId):
    if assId in oldDetails:
        oldDetails[assId][1] = details.get(GRADE_FORM_KEYS[0])
        oldDetails[assId][2] = details.get(GRADE_FORM_KEYS[1])
    return oldDetails
