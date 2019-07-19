from django.conf.urls import url,include
from . import views
from django.views.static import serve

app_name='game'
urlpatterns=[
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^news/$',views.NewsView.as_view(),name='news'),
    url(r'^newsdetail/(\d+)/$',views.NewsdetailView.as_view(),name='newsdetail'),
    url(r'^data/$',views.DataView.as_view(),name='data'),
    url(r'^register/$',views.RegisterView.as_view(),name='register'),
    url(r'^login/$',views.LoginView.as_view(),name='login'),
    url(r'^checkuser/$',views.Checkuser,name='checkuser'),
    url(r'^download/$',views.DownloadView.as_view(),name='download'),
    url(r'^verify/$',views.verify,name='verify'),
]