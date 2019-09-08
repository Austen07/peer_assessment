from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.Home, name='index'),
    url(r'^courses', views.showCourseList, name='GetCourses'),
    url(r'^assignments', views.showAssignmentsList, name='GetAssignments'),
    url(r'^showAssignmentOptions/(?P<success>\w+?)', views.showAssignmentOptions, name='showAssignment'),
    url(r'^assignmentDetails', views.postAssignmentDetails, name='assignmentDetails'),
    url(r'^gradeAssignment', views.gradeAssignment, name='gradeAssignment'),
    url(r'^generateReport', views.generateReport, name='generateReport'),
]
