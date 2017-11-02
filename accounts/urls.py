from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$',views.OneUser.as_view()),
        url(r'^logout/$',views.logout_view, name='logout'),
        url(r'^register/$',views.register_view,name='register')
        ]
        
