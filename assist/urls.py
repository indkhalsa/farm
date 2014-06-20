from django.conf.urls import patterns, url

from assist import views

urlpatterns = patterns('',
    url(r'^$', views.assist, name='assist'),
    url(r'^/add_ItemDetail/$', views.add_ItemDetail, name='add_ItemDetail'), # New Details!
    url(r'^/add_GoodDetail/$', views.add_GoodDetail, name='add_GoodDetail'),

)
