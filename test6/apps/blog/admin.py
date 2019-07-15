from django.contrib import admin
from .models import Ads,Catgory,Article,Tag
from comment.models import Comment
# Register your models here.
admin.site.register(Article)
admin.site.register(Catgory)
admin.site.register(Tag)
admin.site.register(Comment)