from django.db import models

# Create your models here.
class Account(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    grade=models.IntegerField(default=0)
class Hero(models.Model):
    name=models.CharField(max_length=20)
    grade=models.IntegerField(default=0)
    content=models.CharField(max_length=50)
    lskill=models.CharField(max_length=50)
    pskill=models.CharField(max_length=50)
    skillcontent=models.TextField()
    type=models.CharField(max_length=10)
    account=models.ForeignKey(Account,on_delete=models.CASCADE)

class Pet(models.Model):
    name=models.CharField(max_length=20)
    grade=models.IntegerField(default=0)
    phero=models.ForeignKey(Hero,on_delete=models.CASCADE)


class Petdetail(models.Model):
    hp=models.IntegerField(default=10)
    mp=models.IntegerField(default=10)
    quality=models.CharField(max_length=10)
    ptype=models.CharField(max_length=10)
    pet=models.ForeignKey(Pet,on_delete=models.CASCADE)

class Arms(models.Model):
    head=models.CharField(max_length=10)
    chest=models.CharField(max_length=10)
    leg=models.CharField(max_length=10)
    badge=models.CharField(max_length=10)
    feet=models.CharField(max_length=10)
    ahero=models.ForeignKey(Hero,on_delete=models.CASCADE)

class Goods(models.Model):
    gold=models.IntegerField(default=0)
    bluebrick=models.IntegerField(default=0)
    powderbrick=models.IntegerField(default=0)
    ghero=models.ForeignKey(Hero,on_delete=models.CASCADE)

class Othergoods(models.Model):
    commodity=models.CharField(max_length=20)
    gtype=models.CharField(max_length=10)
    goods=models.ForeignKey(Goods,on_delete=models.CASCADE)


class Warsprit(models.Model):
    name=models.CharField(max_length=20)
    grouptype=models.CharField(max_length=20)
    wshero=models.ForeignKey(Hero,on_delete=models.CASCADE)

class Attck(models.Model):
    ma=models.CharField(max_length=10)
    md=models.CharField(max_length=10)
    wa=models.CharField(max_length=10)
    wd=models.CharField(max_length=10)
    warsprit=models.ForeignKey(Warsprit,on_delete=models.CASCADE)

class Ads(models.Model):
    img=models.ImageField(upload_to='ads')
    desc=models.CharField(max_length=20)
    index=models.IntegerField(default=0)
