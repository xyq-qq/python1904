
from django.conf.urls import url
# from .views import index,detail,result
from . import views
app_name='polls'

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^result/(\d+)/$', views.result, name='result'),
]