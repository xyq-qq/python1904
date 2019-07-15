from django.contrib import admin
from .models import *
from comment.models import *
# Register your models here.
import xadmin
class ArticleAdmin:
    style_fields={'body':'ueditor'}
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Ads)
xadmin.site.register(Catgory)
xadmin.site.register(Tag)
xadmin.site.register(Comment)