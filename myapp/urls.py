from django.urls import include, re_path, path
from .views import *

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^about/$', about, name='about'),
    re_path(r'^category/(?P<cat_no>\d+)/$', detail, name='detail'),
    # re_path(r'^contactus\d*/$', contact, name='contact'),
]
