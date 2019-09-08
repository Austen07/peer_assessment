INSTRUCTOR_FORM_KEYS = ['assignmentDeadline', 'assignmentLink', 'assignmentName', 'challengeDeadline',
                        'peerGradingDeadline', 'numberQuestions', 'gradeTypeDisplay', 'assignmentPercentage',
                        'numberGraders', 'message']
GRADE_FORM_KEYS = ['marks', 'justification']

COURSE_ID_KEY = u"courseId"
CREDENTIALS_KEY = u'credentials'
COURSE_NAME_KEY = u'courseName'
ASSIGNMENT_NAME_KEY = u'assignmentName'
ASSIGNMENT_ID_KEY = u'assignmentId'
NO_GRADERS = u'numberGraders'
NO_QUESTIONS = u'numberQuestions'

GRADING_DATA = u'gradingData'
STUDENT_INDEX = u'index'
SHEET_ID_KEY = u'sheetId'

ASSIGNMENT_LINK_SHEET_INDEX = 5
MARKS_START_SHEET_INDEX = 6
SUBMISSION_START_SHEET_INDEX = 3

INSTRUCTOR_FORM_FILE_KEY = 'instructorForm'
ASSIGNMENT_DISTRIBUTION_FILE_KEY = 'assignmentDistribution'

NEW_ASSIGNMENT_OPTION = '3'
OPERATION_SUCCESS = 1
OPERATION_FAILED = 0
OPERATION_FAILED_FETCH = 4

ME_KEY = 'me'

GRADING_SHEET_HEADER = ['UserId', 'Name', 'EmailId', 'GradingAssignmentStudentUserId',
                        'GradingAssignmentStudentEmailId', 'AssignmentLink']
SHEET_BLANK_CELL = ""
SHEET_START_COLUMN = "A"
ROW_1 = "1"
ROW_2 = "2"
SHEET_END_COLUMN = "Z"
RANGE_KEY = u'range'
VALUES_KEY = u'values'
SHEET_VALUE_INPUT_OPTION_RAW = u'RAW'
ASCII_G = 71
ASCII_A = 65

PERMISSION_ROLE_READER = u'reader'
ROLE_KEY = u'role'
TYPE_KEY = u'type'
PERMISSION_TYPE_USER = u'user'

ID_KEY = u'id'
PROFILE_KEY = u'profile'
EMAIL_ADDRESS_KEY = u'emailAddress'
TEACHERS_KEY = u'teachers'
ASSIGNMENT_SUBMISSION_KEY = u'assignmentSubmission'
ATTACHMENTS_KEY = u'attachments'
DRIVEFILE_KEY = u'driveFile'
ALTERNATE_DRIVEFILE_LINK_KEY = u'alternateLink'
USER_ID_KEY = 'userId'
STUDENT_SUBMISSIONS_KEY = u'studentSubmissions'
ASSIGNMENT_KEY = u'assignment'
STUDENT_WORK_FOLDER_KEY = u'studentWorkFolder'
STUDENTS_KEY = u'students'
NAME_KEY = u'name'
FULL_NAME_KEY = u'fullName'
TEACHER_ROLE_KEY = u'TEACHER'
TEACHER_FOLDER_KEY = u'teacherFolder'

NOT_INSTRUCTOR_ERROR_MESSAGE = 'Requested entity was not found.'
MESSAGE_KEY = 'message'
ERROR_KEY = 'error'

ASSIGNMENT_DEADLINE_KEY = u'assignmentDeadline'
ASSIGNMENT_LINK_KEY = u'assignmentLink'
ASSIGNMENT_NAME_KEY = u'assignmentName'
LINK_KEY = u'link'
URL_KEY = u'url'
TITLE_KEY = u'title'
DAY_KEY = u'day'
MONTH_KEY = u'month'
YEAR_KEY = u'year'
HOURS_KEY = u'hours'
MINUTES_KEY = u'minutes'

MATERIALS_KEY = u'materials'
STATE_KEY = u'state'
WORK_TYPE_KEY = u'workType'
DUE_DATE_KEY = u'dueDate'
DUE_TIME_KEY = u'dueTime'
ASSIGNMENT_WORK_TYPE_KEY = u'ASSIGNMENT'
PUBLISHED_STATE_KEY = u'PUBLISHED'
DATE_FORMAT_KEY = '%Y-%m-%dT%H:%M'

GRADE_FORMS_FOLDER_KEY = u'gradeForms'

MIME_TYPE_KEY = u'mimeType'
FOLDER_MIME_TYPE_KEY = u'application/vnd.google-apps.folder'
FOLDER_MIME_TYPE_KEY = u'application/vnd.google-apps.folder'
SPREADSHEET_MIME_TYPE_KEY = u'application/vnd.google-apps.spreadsheet'
PARENTS_KEY = u'parents'

UNDERSCORE_KEY = '_'
FILES_KEY = u'files'

DEFAULT_HOUR = 23
DEFAULT_MINUTE = 59

YOUTUBE_VIDEO_KEY = u'youtubeVideo'
ALTERNATE_LINK_KEY = u'alternateLink'
ASSOCIATED_WITH_DEVELOPER_KEY = u"associatedWithDeveloper"

ASSIGNMENT_PERCENTAGE_KEY = u'assignmentPercentage'

SHEET_USERID_INDEX = 0
SHEET_NAME_INDEX = 1
SHEET_EMAIL_ID_INDEX = 2
SHEET_GRADING_ASSIGNMENT_STUDENT_ID = 3
SHEET_GRADING_ASSIGNMENT_STUDENT_EMAIL_ID = 4
SHEET_ASSIGNMENT_LINK = 5

GRADER_ID_LIST = u'graderIdList'
GRADED_COUNT = u'gradedCount'
GRADE_DEVIATED_COUNT = u'gradeDeviatedCount'
GRADE_TOTAL_COUNT = u'gradeTotalCount'
GRADE_MEAN = u'gradeMean'
GRADE_MEAN_WITH_LEAST_VALUE_REMOVED = u'gradeMeanLeastVal'
GRADE_SCORE = u'score'

SCORE_VARIANCE_PERCENTAGE = 25
PEER_GRADING_VARIANCE_PERCENTAGE = 4

ASSIGNMENT_SCORE_KEY = u'AssignmentScore'
PEER_GRADING_SCORE_KEY = u'PeerGradingScore'
TOTAL_SCORE_KEY = u'TotalScore'
GRADING_DEVIATION = u'GradingDeviation'
REPORT_SHEET_NAME_KEY = u'Report'

SPREADSHEET_URL_KEY = u'spreadsheetUrl'

ASSIGNMENT_DEADLINE_UPDATE_FAIL_MSG = "Fail to update assignment deadline as the assignment was not created using the peer grading portal."


def getQueryToSearchInDrive(fileName, driveLinkId, fileType):
    query = 'name="' + fileName + '" and "' + driveLinkId + '" in parents and mimeType = "' + fileType + '"'
    return query
