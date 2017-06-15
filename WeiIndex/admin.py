#coding:utf-8
from django.contrib import admin
from WeiIndex.models import WeiIndexModel
# Register your models here.

@admin.register(WeiIndexModel)
class WeiIndexAdmin(admin.ModelAdmin):
    list_display = ['name','primary_title','sub_title','state']
    list_editable = ['state']