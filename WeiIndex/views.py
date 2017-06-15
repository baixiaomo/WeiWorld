#coding:utf-8
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from WeiIndex.models import WeiIndexModel
from WeiModel.models import WeiAddressCollection
from django.http import HttpResponse
# Create your views here.

def index(request):
    queryset = WeiIndexModel.objects.filter(state=True)#查询生效模板
    address = WeiAddressCollection.objects.filter(show_in_index=True)
    indexModel=None
    if queryset:
        indexModel = queryset[0]
    return render_to_response('index.html',context={'indexModel':indexModel,'address':address},context_instance=RequestContext(request))
