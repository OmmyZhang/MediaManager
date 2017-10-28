from django.conf.urls import url

from . import views

urlpatterns = [
        url('^.*/$',views.post_center,name='post_center')
        ]
        
