#coding:utf-8
from django.shortcuts import render,render_to_response
from django.template import RequestContext
# Create your views here.
#首页
def portal(request):
    return render_to_response('portal.html',context=None,context_instance=RequestContext(request))