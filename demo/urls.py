#!/usr/bin/env python
from django.conf.urls import patterns, url

from demo import views

urlpatterns = patterns('',
    url(r'^$', views.demo, name='demo')
)
