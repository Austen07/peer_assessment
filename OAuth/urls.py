from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^portalLogin/', views.login, name='portalLogin'),
    url(r'^oauth2callback/', views.auth_return, name='oauth2callback'),
    url(r'^account/logout', views.logout_page, name='logout'),
]