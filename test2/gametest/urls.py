from django.conf.urls import url
from .views import indexview,listview,detailview,deleteview,addgood,addhero,deletehero
app_name='gametest'
urlpatterns=[
    # url(r'^$')
    url(r'^index/$',indexview,name='index'),
    url(r'^list/$',listview,name='list'),
    url(r'^detail/(\d+)/$',detailview,name='detail'),

    url(r'^addhero/$',addhero,name='addhero'),

    url(r'^addgood/(\d+)/$',addgood,name='addgood'),

    url(r'^deletehero/(\d+)/$',deletehero,name='deletehero'),

    url(r'^delete/(\d+)/$',deleteview,name='delete')
]