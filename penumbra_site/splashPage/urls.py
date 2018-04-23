from django.conf.urls import include, url
from django.contrib import admin

from . import views


app_name = 'splashPage'

urlpatterns = [
    url(r'^$', views.splashPage, name='splashPage'),
]