from django.shortcuts import render,reverse,redirect,loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import QuestionsInfo,ChoicesInfo
# Create your views here.
def index(request):
    # return HttpResponse('首页')
    questions=QuestionsInfo.objects.all()
    return render(request,'pollstest/index.html',{'questions':questions})

def detail(request,id):
    # return HttpResponse('问题列表')
    question = QuestionsInfo.objects.get(pk=id)
    if request.method == 'GET':

        return render(request,'pollstest/questions.html',{'question':question})

    elif request.method == 'POST':
        choiceid=request.POST.get('choice')
        choice=ChoicesInfo.objects.get(pk=choiceid)
        choice.votes+=1
        choice.question=question
        choice.save()
        return redirect(reverse('pollstest:result',args=(id,)))

def result(request,id):
    # return HttpResponse('结果页')
    question=QuestionsInfo.objects.get(pk=id)
    return render(request,'pollstest/result.html',{'question':question})

