from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$',views.Upload_file, name='index'),
        url(r'^Upload_file/$',views.Upload_file,name='upload'),
        url(r'^Download_file/$',views.Download_file,name='download'),
        ]
