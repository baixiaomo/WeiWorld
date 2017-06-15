#coding:utf-8
__author__ = 'feiwei'
from django import template

register = template.Library()

@register.filter('split')
def split(value,arg):
    if arg:
        return value.split(arg)
    else:
        return value.split(',')
