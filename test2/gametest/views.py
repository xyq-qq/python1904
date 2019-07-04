from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import HerosInfo,GoodsInfo
from django.views.generic import View,TemplateView
# Create your views here.

# class IndexView(View):
#     def get(self,request):
#         return render(request,'gametest/index.html',{'username':'xyq'})


def indexview(request):
    # return HttpResponse('这是首页')
    temp1=loader.get_template('gametest/index.html')
    result=temp1.render({'username':'xyq'})
    return HttpResponse(result)

def listview(request):
    # return HttpResponse('这是列表')
    heros = HerosInfo.objects.all()
    temp2=loader.get_template('gametest/list.html')
    result=temp2.render({'heros':heros})
    return HttpResponse(result)
def detailview(request,id):
    # return HttpResponse('这是详情页')
    hero=HerosInfo.objects.get(pk=id)
    temp3=loader.get_template('gametest/detail.html')
    result=temp3.render({'hero':hero})
    return HttpResponse(result)


def addhero(request):
    # return HttpResponse('添加成功')
    # return HttpResponseRedirect()
    if request.method=='GET':

        return render(request,'gametest/addhero.html')
    elif request.method=='POST':
        name=request.POST.get('heroname')
        hp=request.POST.get('herohp')
        mp=request.POST.get('heromp')
        gender=request.POST.get('gender')
        type=request.POST.get('type')
        h1=HerosInfo()
        h1.name=name
        h1.hp=hp
        h1.mp=mp
        h1.gender=gender
        h1.type=type
        h1.save()

        return redirect(reverse('gametest:list'))


def addgood(request,id):
    # return HttpResponse('添加成功')
    hero = HerosInfo.objects.get(pk=id)
    if request.method=='GET':
        return render(request,'gametest/addgood.html',{'hero':hero})
    elif request.method=='POST':
        name=request.POST.get('goodname')
        type=request.POST.get('gootype')
        hurt=request.POST.get('hurt')
        g1=GoodsInfo()
        g1.name=name
        g1.type=type
        g1.hurt=hurt
        g1.hero=hero
        g1.save()
        # return HttpResponse('添加成功')
        return redirect(reverse('gametest:detail',args=(id,)))

def deletehero(request,id):
    # return HttpResponse('删除成功')
    hero=HerosInfo.objects.get(pk=id)
    hero.delete()
    # 这是根据路由重定向的
    return redirect(reverse('gametest:list',))
def deleteview(request,id):
    good=GoodsInfo.objects.get(pk=id)
    heroid=good.hero.id
    good.delete()
    # return HttpResponseRedirect('')
    return redirect(reverse("gametest:detail",args=(heroid,)))