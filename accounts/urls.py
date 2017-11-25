from django.conf.urls import url

from . import views
from society import views as sviews

urlpatterns = [
        url(r'^$', views.OneUser.as_view()),
        url(r'^signup/?$', views.Signup.as_view()),
        url(r'^login/?$',  views.Login.as_view()),
        url(r'^logout/?$',  views.Logout.as_view()),
        url(r'^(?P<id>\d+)/?$', views.UserById.as_view()),
        url(r'^(?P<id>\d+)/password/?$', views.Passwd.as_view()),

        url(r'^(?P<id1>\d+)/follower/?$', sviews.getFollowerList.as_view()),
        url(r'^(?P<id1>\d+)/following/?$', sviews.getFolloweeList.as_view()),
	url(r'^(?P<id1>\d+)/following/(?P<id2>\d+)/?$', sviews.followSb.as_view())
        ]
        