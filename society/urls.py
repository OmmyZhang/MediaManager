from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'ment/?', views.commentDealer.as_view()), #both comment is dealt here
    url(r'ment/(?P<id>\d+)/?$', views.deleteComment.as_view()),
    url(r'ollower/?$', views.getFollowerList.as_view()),
    url(r'ollowing/?$', views.getFolloweeList.as_view()),
    url(r'ollowing/(?P<otherID>\d+)/?$', views.followSb.as_view())          #Follow/Unfollow, same function
    #Need a halal check
    ]