from django.shortcuts import render,reverse,redirect,loader
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import BooksInfo,RoleInfo
def index(request):
    # return HttpResponse('首页')
    return render(request,'bookstest/index.html',{'username':'xyq'})

def lists(request):
    # return HttpResponse('列表页')
    books=BooksInfo.objects.all()
    return render(request,'bookstest/lists.html',{'books':books})

def detail(request,id):
    # return HttpResponse('详情页')
    book=BooksInfo.objects.get(pk=id)
    return render(request,'bookstest/detail.html',{'book':book})

def deletebook(request,id):
    book=BooksInfo.objects.get(pk=id)
    book.delete()

    return redirect(reverse('bookstest:lists'))

def deleterole(request,id):
   role=RoleInfo.objects.get(pk=id)
   # print('-----------------------------------------')
   # print(role)
   # bookid这个字段主要用来当删除完数据之后，重定向到这个表中
   bookid=role.book.id
   # print(bookid)
   role.delete()
   return redirect(reverse('bookstest:detail',args=(bookid,)))

def addbook(request):
    if request.method == 'GET':
        return render(request,'bookstest/addbook.html')

    elif request.method == 'POST':
        name=request.POST.get('bookname')
        author=request.POST.get('bookauthor')
        b1=BooksInfo()
        b1.name=name
        b1.author=author
        b1.save()
        return redirect(reverse('bookstest:lists'))

def addrole(request,id):
    book=BooksInfo.objects.get(pk=id)
    if request.method == 'GET':
        return render(request,'bookstest/addrole.html',{'book':book})

    elif request.method == 'POST':
        name=request.POST.get('rolename')
        content=request.POST.get('rolecontent')
        r1=RoleInfo()
        r1.name=name
        r1.content=content
        r1.book=book
        r1.save()

        return redirect(reverse('bookstest:detail',args=(id,)))

