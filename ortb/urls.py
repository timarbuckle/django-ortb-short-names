from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^ortb/', include('shortnames.urls')),
    url(r'^ortb/admin/', include(admin.site.urls)),
)
