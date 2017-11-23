from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/comment[^/]', views.commentDealer.as_view()), #both comment is dealt here
    url(r'^/comment/$', views.deleteComment.as_view()),
    url(r'follower[^/]^$', views.getFollowerList.as_view()),
    url(r'following[^/]^$', views.getFolloweeList.as_view()),
    url(r'/user/1/following/2', views.followSb.as_view)          #Follow/Unfollow, same function
    #Need a halal check
    ]
