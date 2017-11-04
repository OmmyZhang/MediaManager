from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.FileList.as_view()),
        url(r'^(?P<id>\d+)/?$', views.FileById.as_view())
        ]
        
