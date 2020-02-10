from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from DormBackend.views import *

urlpatterns = [
    url(r'^index$', index),
    url(r'^db_config$', db_config),
    url(r'^config$', config)
]