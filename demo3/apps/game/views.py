from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .models import Ads,Notice,News,NewsDetail,Account
from django.core.paginator import Paginator,Page
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# Create your views here.
from django.http import HttpResponse,JsonResponse

class IndexView(View):
    def get(self,request):
        ads=Ads.objects.all()
        print(ads)
        notices=Notice.objects.all()
        print(notices)
        news=News.objects.all()
        print(news)
        return render(request,'game/index.html',locals())
# def getpage(request,object_list,per_num):
#     pagenum = request.GET.get('page')
#     pagenum = 1 if not pagenum else pagenum
#     page = Paginator(object_list, per_num).get_page(pagenum)
#     return page
class NewsView(View):
    def get(self,request):
        news = News.objects.all()
        print(news)
        notices = Notice.objects.all()
        print(notices)
        paginator=Paginator(news,1)
        print(paginator)
        # print(paginator.page_range)
        # print(paginator.object_list)
        # print(paginator.num_pages)
        # print(paginator.count)
        # page=paginator.get_page(1)
        # print(page)
        # print(page.paginator is paginator)
        # print(page.object_list)
        # print(page.number)
        # print(page.next_page_number)
        # print(page.previous_page_number)
        # print(page.has_previous())
        # print(page.has_next())

        pagenum=request.GET.get('page')
        print(pagenum,'=======================')
        pagenum=1 if not pagenum else pagenum
        page=paginator.get_page(pagenum)
        print(page)
        return render(request,'game/news.html',locals())

class NewsdetailView(View):
    def get(self,request,id):
        new=News.objects.get(pk=id)
        newsdetails=NewsDetail.objects.all()
        return render(request,'game/news_detail.html',locals())

class DataView(View):
    def get(self,request):

        return render(request,'game/data.html')

class RegisterView(View):
    def get(self,request):
        return render(request,'game/account.html')
    def post(self,request):
        username=request.POST.get('name')
        print(username)
        password=request.POST.get('password')
        print(password)
        a=Account()
        a.name=username
        a.password=password
        a.grade=0
        a.save()
        return JsonResponse({'title':'注册成功'})

class LoginView(View):
    def get(self,request):
        return render(request,'game/index.html')
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        accounts=Account.objects.all()
        print(accounts)
        for i in accounts:
            print(i.id,'--------------------------')
            print(i.name,i.password,'-----------------------------')
            if i.name == username and i.password == password:

                return render(request,'game/index.html')
            # else:
            #     return render(request,'game/account.html')

def Checkuser(request):
    if request.method == 'GET':
        name=request.GET.get('name')
        user=Account.objects.filter(name=name).first()

        if user:
            return JsonResponse({'state':1})
        else:
            return JsonResponse({'state':0,'errorinfo':'用户名不存在'})

class DownloadView(View):
    def get(self,request):
        return render(request,'game/download.html')



