from django.contrib import admin
from .models import QuestionInfo,choiceInfo
# Register your models here.

admin.site.register(QuestionInfo)
admin.site.register(choiceInfo)