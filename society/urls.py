from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$',views.comment.as_view()),
        url(r'^(?P<id>\d+)/?$',views.comment.as_view())
    ]
