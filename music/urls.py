
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.index, name='index'),

    #music/id/
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
]
