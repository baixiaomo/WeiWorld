#coding:utf-8
from django.shortcuts import render,render_to_response
from django.template import RequestContext

# Create your views here.

def about(request):
    return render_to_response('aboutme.html',context=None,context_instance=RequestContext(request))