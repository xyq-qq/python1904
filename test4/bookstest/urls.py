from django.conf.urls import url
from .views import index,lists,detail,deleterole,deletebook,addbook,addrole
app_name='bookstest'

urlpatterns=[
    url(r'^$',index,name='index'),
    url(r'^lists/$',lists,name='lists'),
    url(r'^detail/(\d+)/$',detail,name='detail'),

    url(r'^addbook/$',addbook,name='addbook'),
    url(r'^addrole/(\d+)/$',addrole,name='addrole'),

    url(r'^deletebook/(\d+)/$',deletebook,name='deletebook'),
    url(r'^deleterole/(\d+)/$',deleterole,name='deleterole'),
]
