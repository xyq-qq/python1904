from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BookInfo,HeroInfo
# Create your views here.
def myview(request):
    # return HttpResponse("<h2 style='color:red; align:center;'>这是自定义路由展示界面</h2>  <a  href='/booktest/youurl/'><h1> 跳转到你的路由</h1></a>")

    temp1=loader.get_template('booktest/index.html')
    result=temp1.render({"用户名":'zzy'})
    return HttpResponse(result)
def youview(request):
    # return HttpResponse("这是你的自定义路由界面  <a href='/booktest/theyurl/'>跳转到他们的路由</a>")
    # 1.获取模板
    books = BookInfo.objects.all()
    temp2=loader.get_template('booktest/list.html')
    # 2.使用模板渲染字典参数
    result=temp2.render({"books":books})
    # 3.将渲染的结果返回
    return HttpResponse(result)
def theyview(request,id):
    # return HttpResponse("%s这是他们的自定义路由   <a href='/booktest/myurl/'>跳转到我的路由</a> "%(id,))
    book=BookInfo.objects.get(pk=id)
    temp3=loader.get_template('booktest/detail.html')
    result=temp3.render({'book':book})
    return HttpResponse(result)

