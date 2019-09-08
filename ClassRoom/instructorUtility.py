from datetime import datetime
from service import getClassRoomService, getDriveService
from PeerReview.Logger import getLogger
from keyConstants import *
from mail import SendMessage

log = getLogger("instructorUtility")


def createAssignment(credentials, courseId, assignmentDetails):
    """
    Create google classroom coursework using the configration given by the teacher
    Arguments:
        credentials: access to Google API
        assignmentDetails: Assignment configuration given by the teacher
    """
    try:
        assignmentDeadline = assignmentDetails[ASSIGNMENT_DEADLINE_KEY]
        assignmentLink = assignmentDetails[ASSIGNMENT_LINK_KEY]
        assignmentTitle = assignmentDetails[ASSIGNMENT_NAME_KEY]
        requestBody = createRequestBodyForAssignmentCreation(assignmentDeadline, assignmentLink, assignmentTitle)
        classroomService = getClassRoomService(credentials)
        courseWorkCreateResponse = classroomService.courses().courseWork().create(courseId=courseId,
                                                                                  body=requestBody).execute()
        return courseWorkCreateResponse[ID_KEY]
    except Exception as err:
        raise type(err)("Failed to create courseWork " + err.message)


def createRequestBodyForAssignmentCreation(assignmentDeadline, assignmentLink, assignmentTitle):
    """
    Return the request body dictionary for the assignment creation
    """
    materialsBody = []
    materialsDict = {}
    materialsLinkDict = {}
    materialsLinkDict[URL_KEY] = assignmentLink
    materialsLinkDict[TITLE_KEY] = assignmentTitle
    materialsDict[LINK_KEY] = materialsLinkDict
    materialsBody.append(materialsDict)
    dt = datetime.strptime(assignmentDeadline, DATE_FORMAT_KEY)
    dueDateBody = {}
    dueDateBody[DAY_KEY] = dt.day
    dueDateBody[MONTH_KEY] = dt.month
    dueDateBody[YEAR_KEY] = dt.year
    dueTimeBody = {}
    dueTimeBody[HOURS_KEY] = dt.hour
    dueTimeBody[MINUTES_KEY] = dt.minute
    requestBody = {MATERIALS_KEY: materialsBody, TITLE_KEY: assignmentTitle, STATE_KEY: PUBLISHED_STATE_KEY,
                   WORK_TYPE_KEY: ASSIGNMENT_WORK_TYPE_KEY, ASSOCIATED_WITH_DEVELOPER_KEY: True,
                   DUE_DATE_KEY: dueDateBody, DUE_TIME_KEY: dueTimeBody}
                   
    return requestBody


def getInstructorEmailList(service, courseId):
    """
    Return the list of teacher's emailId
    """
    instructorsListResponse = service.courses().teachers().list(courseId=courseId).execute()
    instructorsListResponse = instructorsListResponse.get(TEACHERS_KEY)
    instructorsEmailList = []
    for instructorInfo in instructorsListResponse:
        instructorsEmailList.append(instructorInfo[PROFILE_KEY][EMAIL_ADDRESS_KEY])
    log.info("Instructor email list is generated.")
    return instructorsEmailList
