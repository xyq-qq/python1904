from django.shortcuts import render,reverse,redirect,loader
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

class IndexView(View):

    def get(self,request):
        return render(request,'gametest/index.html')
