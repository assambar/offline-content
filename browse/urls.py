from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dir/(?P<dir_id>[0-9]+)/$', views.dirContent, {'refresh': False}, name='dirContent'),
    url(r'^dir/(?P<dir_id>[0-9]+)/refresh$', views.dirContent, {'refresh': True}, name='dirContent'),
    url(r'^show/file/(?P<file_id>[0-9]+)/$', views.showFile, name='showFile'),
    url(r'^raw/file/(?P<file_id>[0-9]+)/$', views.downloadFile, name='downloadFile'),
    url(r'^raw/file/(?P<file_id>[0-9]+)/stream$', views.streamFile, name='streamFile')
]
