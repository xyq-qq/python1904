from django.db import models

# Create your models here.
class QuestionsInfo(models.Model):
    desc=models.CharField(max_length=50)
    pub_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc

class ChoicesInfo(models.Model):
    desc=models.CharField(max_length=50)
    votes=models.IntegerField()
    question=models.ForeignKey(QuestionsInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.desc