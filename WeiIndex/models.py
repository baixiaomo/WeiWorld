#coding:utf-8
from django.db import models
from WeiModel.models import WeiEssay
from WeiModel.constant import *
# Create your models here.

'''
index页面模型
'''
class WeiIndexModel(models.Model):
    name = models.CharField(max_length=20,blank=False,default='模板')#模板名称
    primary_title = models.CharField(max_length=20,default='我的微世界') #主标题
    sub_title = models.CharField(max_length=50,default='副标题')#副标题
    enter_button_text = models.CharField(max_length=20,default='进入世界')#进入按钮文本
    state = models.BooleanField(default=False)#是否激活
    loginUrl = models.URLField(default='')#后台管理页面链接
    primary_title2_left = models.CharField(max_length=20,default='常用链接') #主标题
    primary_title2_right = models.CharField(max_length=20,default='百小陌') #主标题
    sub_title2 = models.CharField(max_length=50,default='总有一些文字想要留下')#副标题
    about_button_text = models.CharField(max_length=20,default='关于我')#进入按钮文本
    display_essay = models.ForeignKey(WeiEssay,on_delete=models.CASCADE,default=1)
    creator = models.CharField('创建者',max_length=20,blank=True)
    updater = models.CharField('修改者',max_length=20,blank=True)
    createTime = models.DateTimeField('创建时间',auto_now_add=True,blank=True,null=True)
    updateTime = models.DateTimeField('更新时间',blank=True,null=True)

    def __str__(self):
        return self.name

    def createTimeFormat(self):
        if self.createTime:
            return self.createTime.strftime(WEI_DATE_TIME_PATTERN)
        return ''
    def updateTimeFormat(self):
        if self.updateTime:
            return self.updateTime.strftime(WEI_DATE_TIME_PATTERN)
        return ''
    class Meta:
        verbose_name = u'[进入微世界]页面'
        verbose_name_plural = u'[进入微世界]页面'


