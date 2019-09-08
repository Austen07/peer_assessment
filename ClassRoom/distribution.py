from random import shuffle
from PeerReview.Logger import getLogger
from service import getClassRoomService, getDriveService, getSheetService
from mail import SendMessage
from keyConstants import *
from instructorUtility import getInstructorEmailList

log = getLogger("distribution")

# courseId is the id of course
# courseworkId is the id of assignment

def getStudentSubmissionList(service, courseId, courseWorkId):
    """
    arguments: 
        service: used to access Google Classroom
    return: 
        A list of student submission
    """
    studentSubmissionListResponse = service.courses().courseWork().studentSubmissions().list(courseId=courseId,
                                                                                             courseWorkId=courseWorkId).execute()
    studentSubmissionList = studentSubmissionListResponse.get(STUDENT_SUBMISSIONS_KEY)
    log.info("Student Submission list is generated for the assignment : %s", courseWorkId)
    return studentSubmissionList


def getDistributionData(service, courseId, courseWorkId):
    """
    Generates the distribution data to randomly assign assignment among students
    Arguments:
     service: access Google Classroom
    return: 
        A tuple containing a list of userIds of all the students
        A dictionary with student submissions with userId as key
    """
    studentSubmissionList = getStudentSubmissionList(service, courseId, courseWorkId)
    updateStudentSubmissionList = [d for d in studentSubmissionList if ATTACHMENTS_KEY in d[ASSIGNMENT_SUBMISSION_KEY]]
    userIdList = [unicode(d[USER_ID_KEY]) for d in updateStudentSubmissionList]
    log.info("UserID list is generated for course %s and courseWork %s", courseId, courseWorkId)
    studentSubmissionsDic = {}
    for studentSubmission in updateStudentSubmissionList:
        studentSubmissionsDic[studentSubmission[USER_ID_KEY]] = studentSubmission
    log.info("Data for random distribution is generated for courseId %s and courseWorkdId %s", courseId, courseWorkId)
    return (userIdList, studentSubmissionsDic)


def randomDistribute(credentials, paramDic, courseId, courseName, courseWorkId, courseWorkName, studentData):
    """
    Randomly distibute assignments
    Arguments:
        credentials: access Google Sheet API.
        paramDic: the configuration parameter dictionary
        studentData : dictionary containing student information with userId as the key
    return: 
        A dictionary containing randomly distributed assignments.
    """
    try:
        service = getClassRoomService(credentials)
        (userIdList, studentSubmissionsDic) = getDistributionData(service, courseId, courseWorkId)
        shuffle(userIdList)
        randomIndexDic = randomize(len(userIdList), int(paramDic[NO_GRADERS]))
        assignmentListDic = {}
        studentEmailList = []

        for key in randomIndexDic.keys():
            keySubList = []
            userId = userIdList[key]
            emailId = studentData[userId].get(PROFILE_KEY)[EMAIL_ADDRESS_KEY]
            serviceDrive = getDriveService(credentials)
            for index in randomIndexDic[key]:
                attachments = studentSubmissionsDic[userIdList[index]][ASSIGNMENT_SUBMISSION_KEY][ATTACHMENTS_KEY]
                assignmentEmailId = studentData[userIdList[index]][PROFILE_KEY][EMAIL_ADDRESS_KEY]
                driveLink = ""
                for attachment in attachments:
                    if DRIVEFILE_KEY in attachment:
                        link = attachment[DRIVEFILE_KEY][ALTERNATE_DRIVEFILE_LINK_KEY]
                    elif LINK_KEY in attachment:
                        link = attachment[LINK_KEY][URL_KEY]
                    driveLink += link + ","
                tuple = (userIdList[index], assignmentEmailId, driveLink[:-1])
                keySubList.append(tuple)
            assignmentListDic[userId] = keySubList
            studentEmailList.append(emailId)
        instructorEmailList = getInstructorEmailList(service, courseId)
        sendMail(credentials, studentEmailList, instructorEmailList, paramDic['message'], courseName, courseWorkName)
        log.info("Distribution of assignment among students successful for courseId %s and courseWorkdId %s", courseId,
                 courseWorkId)
        return assignmentListDic
    except Exception as ex:
        log.error("Unable to distribute assignment among students %s", str(ex))


def randomize(num_assignments, num_graders_per_assignment):
    """
    Arguments:
        num_assignments: Total number of assignments
        num_graders_per_assignment: Number of assignments per grader/Number of graders per assignment
    return: 
        A dictionary of random indexes.
    """
    result = {}
    for i in range(0, num_assignments):
        assigned_graders = []
        for j in range(0, num_graders_per_assignment):
            assigned_graders.append((i + j + 1) % num_assignments)
        result[i] = assigned_graders
    log.info("Randomize distribution of assignments is completed.")
    return result


def sendMail(credentials, studentEmailList, instructorEmailList, emailMessage, courseName, courseWorkName):
    """
    Send email to all the teachers(CC) and students(BCC).
    Arguments:
        credentials: access to Google Mail API
        studentEmailList: List of student Email Id.
        instructorEmailList: List of Teacher's email Id
        emailMessage: Email Message to be added in the mail
    """
    bcc = ",".join(studentEmailList)
    to = ",".join(instructorEmailList)
    # TODO: Change sender.
    sender = ME_KEY
    subject = courseName + " : " + courseWorkName + " grading assignment"
    msgHtml = emailMessage
    msgPlain = " "
    SendMessage(credentials, sender, to, bcc, subject, msgHtml, msgPlain)
