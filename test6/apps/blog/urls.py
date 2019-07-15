
from django.conf.urls import url
from django import views
from .views import IndexView,SingleView,AddArticleView
app_name='blog'

urlpatterns=[
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^single/(\d+)/$',SingleView.as_view(),name='single'),

    url(r'^addarticle/$',AddArticleView.as_view(),name='addarticle'),
]