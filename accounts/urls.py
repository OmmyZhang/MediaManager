from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.OneUser.as_view()),
        url(r'^signup/?$', views.Signup.as_view()),
        url(r'^login/?$',  views.Login.as_view()),
        url(r'^logout/?$',  views.Logout.as_view()),
        url(r'^(?P<id>\d+)/?$', views.UserById.as_view()),
        url(r'^(?P<id>\d+)/password/?$', views.Passwd.as_view()),

        url(r'^(?P<id1>\d+)/follower/?$', views.getFollowerList.as_view()),
        url(r'^(?P<id1>\d+)/following/?$', views.getFolloweeList.as_view()),
	url(r'^(?P<id1>\d+)/following/(?P<id2>\d+)/?$', views.followSb.as_view())
        ]
        
