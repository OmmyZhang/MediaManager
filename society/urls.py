from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$',views.haha.as_view(),name='haha'),
        url(r'^(?P<id>\d+)/?$',views.deleteComment.as_view(),name='id')
    ]
