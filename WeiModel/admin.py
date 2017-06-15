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



#跳转到index页面
admin.site.site_url = '/weiworld/'



