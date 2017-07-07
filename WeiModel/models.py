#coding:utf-8
from django.db import models
from django.utils import timezone
# Create your models here.
#{收藏网址}模型设计
class WeiAddressCollection(models.Model):
    id = models.AutoField(primary_key=True)#主键
    name = models.CharField('地址名称',max_length=20,default='')
    desc = models.CharField('地址描述',max_length=100,default='')
    url = models.URLField('地址链接',default='')
    type = models.IntegerField(default=0)#地址类型
    tags = models.CharField('地址标签',max_length=50,default='')
    state = models.CharField('状态',max_length=2,default='')
    show_in_index = models.BooleanField('是否显示在index页面',default=False)
    creator = models.CharField('创建者',max_length=20,default='')
    updater = models.CharField('修改者',max_length=20,default='')
    createTime = models.DateTimeField('创建时间',auto_now=True)
    updateTime = models.DateTimeField('更新时间',auto_now_add=True)

    def __str__(self):
        return self.name

#{收藏文件}模型设计
class WeiFilesCollection(models.Model):
    fileName = models.CharField(max_length=100)    #文件名称
    fileType = models.CharField(max_length=2)  #文件类型，音频，视频，图片等
    filePath = models.FileField(upload_to='uploads/%Y/%m/%d/') #文件位置
    uploadTime = models.DateTimeField(auto_now=True) #文件上传时间
    uploader = models.CharField(max_length=20)  #文件上传者
    fileState = models.CharField(max_length=2)  #文件状态
    fileSort = models.IntegerField()   #文件分类

    def __str__(self):
        return self.fileName

#{个人文章}模型设计
class WeiEssay(models.Model):
    name = models.CharField('文章名称',max_length=20,default='')
    content = models.TextField('文章内容')
    author = models.CharField('文章作者',max_length=20)
    type = models.IntegerField(default=0)#文章分类
    tags = models.CharField('文章标签',max_length=50,default='')
    state = models.CharField('状态',max_length=2,default='')
    creator = models.CharField('创建者',max_length=20,default='')
    updater = models.CharField('修改者',max_length=20,default='')
    createTime = models.DateTimeField('创建时间',auto_now=True)
    updateTime = models.DateTimeField('更新时间',auto_now_add=True)
    def __str__(self):
        return self.name
#数据字典模型
class WeiDictionary(models.Model):
    type = models.CharField('字典大类',max_length=100)
    type_desc = models.CharField('字典大类描述',max_length=100)
    code = models.CharField('字典CODE',max_length=100)
    code_desc = models.CharField('CODE描述',max_length=100)
    create_time = models.DateTimeField('字典创建时间',auto_now=True)
    modify_time = models.DateTimeField('字典修改时间',auto_now_add=True)
    creator = models.CharField('创建者',max_length=100)
    modifier = models.CharField('修改者',max_length=100,blank=True)
    state = models.BooleanField('状态',default=True)

    class Meta:
        verbose_name = u'数据字典管理'
        verbose_name_plural = u'数据字典管理'

