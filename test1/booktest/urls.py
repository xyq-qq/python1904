
from django.conf.urls import url
from .views import myview,youview,theyview
# 这是应用路由配置
urlpatterns=[
    url(r'^myurl/$',myview),
    url(r'^youurl/$',youview),
    url(r'^theyurl/(\d+)/',theyview),
]