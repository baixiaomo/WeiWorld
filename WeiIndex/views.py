#coding:utf-8
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from WeiIndex.models import WeiIndexModel
from django.http import HttpResponse
# Create your views here.

def index(request):

    queryset = WeiIndexModel.objects.filter(state=True)#查询生效模板
    print(queryset)
    print([p.name for p in queryset])

    return render_to_response('index.html',context={'indexModel':queryset},context_instance=RequestContext(request))
