from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', post_list, name = "list"),
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name = 'detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name = 'update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    # url(r'^(?P<slug>\d+)/$', post_detail, name = "detail"),
    # url(r'^(?P<slug>\d+)/edit/$', post_update, name = "update"),
    # url(r'^(?P<slug>\d+)/delete/$', post_delete),
]
