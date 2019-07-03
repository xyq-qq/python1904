from django.contrib import admin
from .models import *
# Register your models here.

class HeroInfoINlines(admin.StackedInline):
    model = HeroInfo
    extra = 1
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ('title','pad_date')
    list_filter = ('title','pad_date')
    list_per_page = 1
    search_fields = ('name','content')
    inlines = [HeroInfoINlines,]
admin.site.register(BookInfo,BookInfoAdmin)

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ('name','gender','content','book')
    list_filter = ('name','content','book')
admin.site.register(HeroInfo,HeroInfoAdmin)
