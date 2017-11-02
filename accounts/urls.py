from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.OneUser.as_view()),
        url(r'^signup/$', views.Signup.as_view()),
        url(r'^login/$', views.Login.as_view()),
        ]
        
