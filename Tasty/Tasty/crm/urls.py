from django.conf.urls import url
from crm import views

urlpatterns = [
    url(r'^login/$',views.login, name='login'),
]