from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^addfriend$', views.add_friend),
    url(r'^checkfriends$', views.check_friends),
]
