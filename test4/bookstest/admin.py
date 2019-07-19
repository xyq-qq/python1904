from django.contrib import admin
from .models import BooksInfo,RoleInfo
# Register your models here.


class RoleInfolines(admin.StackedInline):
    model =RoleInfo
    extra = 1
class BooksAdmin(admin.ModelAdmin):
    list_display = ('name','pub_time')
    list_filter = ('name','pub_time')
    list_per_page = 1
    search_fields = ('name','pub_time')
    inlines = [RoleInfolines]
admin.site.register(BooksInfo,BooksAdmin)



class RoleAdmin(admin.ModelAdmin):
    list_display = ('name','content')
    list_filter = ('name','content')
    list_per_page = 1
    search_fields = ('name','content')


admin.site.register(RoleInfo,RoleAdmin)