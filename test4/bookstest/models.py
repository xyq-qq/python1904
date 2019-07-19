from django.db import models

# Create your models here.
class BooksInfo(models.Model):
    name=models.CharField(max_length=50)
    pub_time=models.DateTimeField(auto_now_add=True)
    author=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class RoleInfo(models.Model):
    name=models.CharField(max_length=20)
    content=models.CharField(max_length=100)
    book=models.ForeignKey(BooksInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

