from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^assist/', include('assist.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_ItemDetail/', include('assist.urls')),
    url(r'^add_GoodDetail/', include('assist.urls')),
)
