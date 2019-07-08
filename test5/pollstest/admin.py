from django.contrib import admin
from .models import QuestionsInfo,ChoicesInfo
# Register your models here.




class ChoicesInfolines(admin.StackedInline):
    model = ChoicesInfo
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('desc','pub_time')
    list_filter = ('desc','pub_time')
    list_per_page = 1
    search_fields = ('desc','pub_time')
    inlines = [ChoicesInfolines]
admin.site.register(QuestionsInfo,QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('desc','votes')
    list_filter = ('desc','votes')
    list_per_page = 1
    search_fields = ('desc','votes')

admin.site.register(ChoicesInfo,ChoiceAdmin)


