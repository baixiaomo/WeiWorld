#coding:utf-8
from django.db import models

# Create your models here.

'''
index页面模型
'''
class WeiIndexModel(models.Model):
    name = models.CharField(max_length=20,blank=False)#模板名称
    primary_title = models.CharField(max_length=20,default='我的微世界') #主标题
    sub_title = models.CharField(max_length=50)#副标题
    enter_button_text = models.CharField(max_length=20)#进入按钮文本
    state = models.BooleanField()#是否激活

    def __str__(self):
        return self.name


