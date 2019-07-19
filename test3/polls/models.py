from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class QuestionInfo(models.Model):
    desc=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)

class choiceInfo(models.Model):
    desc=models.CharField(max_length=100)
    votes=models.IntegerField()
    question=models.ForeignKey(QuestionInfo,on_delete=models.CASCADE)


class Myuser(models.Model):
    username=models.CharField(max_length=20)
    acc=models.OneToOneField(User,on_delete=models.CASCADE)

class Account(models.Model):
    account=models.CharField(max_length=20)

class Person(models.Model):
    person=models.CharField(max_length=20)
    acco=models.OneToOneField(Account,on_delete=models.CASCADE)

