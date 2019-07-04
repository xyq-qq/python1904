from django.db import models
# Create your models here.

class HerosInfo(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=5,choices=(('man','男'),('woman','女')),default='man')
    type=models.CharField(max_length=5,choices=(('close','近战'),('near','远战')),default='近战')
    hp=models.CharField(max_length=20)
    mp=models.CharField(max_length=20)

class GoodsInfo(models.Model):
    name=models.CharField(max_length=20)
    type=models.CharField(max_length=20)
    hurt=models.CharField(max_length=20)
    hero=models.ForeignKey(HerosInfo,on_delete=models.CASCADE)
