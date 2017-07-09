# coding:utf-8
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Tasty.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^novel/', include('novel.urls', namespace='novel')),
    url(r'^job/', include('job.urls', namespace='job')),
    url(r'^crm/', include('crm.urls', namespace='crm')),
    # url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),  #配置返回的图标，不配置的话浏览器会使用默认图标，这个方法在django 1.10中会被废弃
]
