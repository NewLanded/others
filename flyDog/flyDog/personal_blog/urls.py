from django.conf.urls import include, url
from personal_blog import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'flyDog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^blog_detail/(?P<blog_id>\d+)/$', views.blog_detail, name='blog_detail'),
    url(r'^blog_wiki/(?P<wiki_id>\d+)/$', views.blog_wiki, name='blog_wiki'),
    url(r'^blog_search/$', views.blog_search, name='blog_search'),
]
