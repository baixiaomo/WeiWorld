#coding:utf-8
from django.db import models
from WeiModel.models import WeiEssay
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
    #page1_background_img_url = models.ImageField(upload_to='upload/',blank=True)#页面1背景图地址
    #page2_background_img_url = models.ImageField(upload_to='upload/',blank=True)#页面2背景图地址
    primary_title2_left = models.CharField(max_length=20,default='常用链接') #主标题
    primary_title2_right = models.CharField(max_length=20,default='百小陌') #主标题
    sub_title2 = models.CharField(max_length=50,default='总有一些文字想要留下')#副标题
    about_button_text = models.CharField(max_length=20,default='关于我')#进入按钮文本
    display_essay = models.ForeignKey(WeiEssay,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.name


