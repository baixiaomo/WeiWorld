#coding:utf-8
__author__ = 'feiwei'

from django.conf.urls import patterns,url

urlpatterns = patterns('WeiAbout.views',
    url(r'^about/$','about'),
)