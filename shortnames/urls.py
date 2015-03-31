from django.conf.urls import patterns, url

from shortnames import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'json/$', views.show_json_keynames, name='json'),
)
