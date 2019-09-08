from django import forms
from Models import *


class CourseListForm(forms.Form):
    courseList = forms.ChoiceField(required=True)

    def __init__(self, courses, *args, **kwargs):
        super(CourseListForm, self).__init__(*args, **kwargs)
        courseList = []
        for course in courses:
            courseList.append((course['id'], course['name']), )
        self.fields['courseList'].choices = courseList


class CourseWorkForm(forms.Form):
    courseWork = forms.ChoiceField(required=True)

    def __init__(self, courseWorks, name, id, cred, *args, **kwargs):
        super(CourseWorkForm, self).__init__(*args, **kwargs)
        courseWorkList = []
        for courseWork in courseWorks:
            courseWorkList.append((courseWork['id'], courseWork['title']), )
        self.fields['courseWork'].choices = courseWorkList
        self.courseName = name
        self.courseId = id
        if isTeacher(cred, id):
            self.createAssignmentOption = True


class AssignmentDetailsForm(forms.Form):
    def __init__(self, courseName, courseId, assignmentName, *args, **kwargs):
        super(AssignmentDetailsForm, self).__init__(*args, **kwargs)
        self.courseName = courseName
        self.courseId = courseId
        self.assignmentName = assignmentName


class StudentAssignmentForm(forms.Form):
    def __init__(self, courseName, courseId, assignmentName, assIds, *args, **kwargs):
        super(StudentAssignmentForm, self).__init__(*args, **kwargs)
        self.courseName = courseName
        self.courseId = courseId
        self.assignmentName = assignmentName
        self.count = assIds


class GradeAssignmentForm(forms.Form):
    def __init__(self, assignmentName, assignmentIndex, gradingData, questionsCount, *args, **kwargs):
        super(GradeAssignmentForm, self).__init__(*args, **kwargs)
        self.assignmentName = assignmentName
        self.assId = assignmentIndex
        # self.assignmentLink = gradingData[assignmentIndex][0]
        self.assignmentDetails = gradingData[assignmentIndex]
        self.count = range(1, int(questionsCount) + 1)
