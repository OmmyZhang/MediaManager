from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$',views.comment.as_view(),name='comment'),
        url(r'^(?P<id>\d+)/?$',views.deleteComment.as_view(),name='id')
    ]
