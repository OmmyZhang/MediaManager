from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.TheGroup.as_view()),
        url(r'^(?P<pk>\d+)/?$', views.GroupById.as_view())
        ]
        
