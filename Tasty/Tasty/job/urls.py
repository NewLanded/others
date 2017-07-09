from django.conf.urls import url
from job import views

urlpatterns = [
    url(r'^joblist_app/$', views.joblist_app, name='joblist_app'),
    url(r'^jobinfo_app/$', views.jobinfo_app, name='jobinfo_app'),
]