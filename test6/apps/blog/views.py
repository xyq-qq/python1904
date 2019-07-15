from django.shortcuts import render,redirect,reverse
from .models import Ads,Catgory,Tag,Article
from comment.models import Comment
from django.http import HttpResponse
from django.views import View
from django.core.paginator import Paginator,Page

# Create your views here.
class IndexView(View):
    def get(self,request):
        ads = Ads.objects.all()
        articles=Article.objects.all()
        paginator=Paginator(articles,1)
        # print(paginator.page_range)
        # print(paginator.object_list)
        # print(paginator.num_pages)
        # print(paginator.count)
        #
        # page=paginator.get_page(3)
        # print(page)
        # print(page.paginator is paginator)
        # print(page.object_list)
        # print(page.number)
        # print(page.next_page_number)
        # print(page.previous_page_number)
        # print(page.has_other_pages)
        # print(page.has_next())
        # print(page.has_previous())
        pagenum=request.GET.get('page')
        print(pagenum)
        pagenum=1 if not pagenum else pagenum
        page=paginator.get_page(pagenum)
        return render(request,'blog/index.html',{'page':page})

class SingleView(View,id):

    def get(self,request,id):
        articles = Article.objects.all()
        return render(request,'blog/single.html')

    def post(self,request,id):
        return render(request,'blog/single.html')

class AddArticleView(View):
    def get(self,request):
        return render(request,'blog/addarticle.html')

    def post(self,request):
        return HttpResponse('添加成功')