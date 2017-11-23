from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.FileList.as_view()),
        url(r'^(?P<pk>\d+)/?$', views.FileById.as_view()),
        url(r'^(?P<pk>\d+)/data/?$',views.FileData.as_view()),
        url(r'^tag/?$',views.TagList.as_view()),
        url(r'^tag/(?P<pk>\d+)/?$', views.TagById.as_view())
        ]
        
