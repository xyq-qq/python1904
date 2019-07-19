from django.shortcuts import render,reverse,redirect,loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import QuestionInfo,choiceInfo
# Create your views here.
def index(request):
    # return HttpResponse('首页')
    questions=QuestionInfo.objects.all()
    return render(request,'polls/index.html',{'questions':questions})

def detail(request,id):
    # return HttpResponse('详情页')
    q=QuestionInfo.objects.get(pk=id)
    print('+++++++++++++++++++++')
    print(q)
    print(q.id)
    print('-----------------------')
    if request.method == 'GET':
        return render(request,'polls/detail.html',{'question':q})
    elif request.method == 'POST':
        choice=choiceInfo.objects.get(pk=id)
        desc=request.POST.get('desc')
        choice.desc=desc
        choice.votes +=1
        choice.question=q.id
        choice.save()
        return redirect(reverse('polls:detail',args=(id,)))



def result(request,id):
    # return HttpResponse('结果页')
    question = QuestionInfo.objects.get(pk=id)
    return render(request,'polls/result.html',{'question':question})



def login(request):
    if request.method == 'GET':
        return render(request,'polls/login.html')

    elif request.method == 'POST':
        return redirect(reverse('polls:index'))