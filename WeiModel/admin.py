from django.contrib import admin
from WeiModel.models import WeiAddressCollection,WeiDictionary,WeiEssay,WeiFilesCollection

# Register your models here.
@admin.register(WeiAddressCollection)
class WeiAddressCollectionAdmin(admin.ModelAdmin):
    list_display = ['id','name','desc','type','state']

@admin.register(WeiEssay)
class WeiEssayAdmin(admin.ModelAdmin):
    list_display = ['name','content','type']

@admin.register(WeiFilesCollection)
class WeiFilesCollection(admin.ModelAdmin):
    list_display = ['fileName','fileType','filePath','uploadTime','fileState','fileSort',]

@admin.register(WeiDictionary)
class WeiDictionaryAdmin(admin.ModelAdmin):
    list_display = ['id','type','type_desc','code','code_desc']


#-----------------------------------站点基本设置
#跳转到index页面
admin.site.site_url = '/weiworld/'
#登陆模板
admin.site.login_template='admin/login.html'
#后台header
admin.site.site_header='微世界后台管理系统'
#管理页面index
admin.site.index_title='我的微世界'



