#coding:utf-8
from django.contrib import admin
from WeiIndex.models import WeiIndexModel
# Register your models here.

@admin.register(WeiIndexModel)
class WeiIndexAdmin(admin.ModelAdmin):
    #-----------------------------------list页面设置start------------------------------------------
    #list展示字段
    list_display = ['name','primary_title','sub_title','state','createTimeFormat','updateTimeFormat']
    #list可编辑字段
    list_editable = ['state']
    #搜索栏
    search_fields = ('name','primary_title',)
    #时间导航
    # date_hierarchy = 'createTime'
    #取消删除ACTION

