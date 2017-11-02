from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.OneUser.as_view()),
        url(r'^signup/$', views.signup_view),
        url(r'^login/$', views.login_view),
        ]
        
