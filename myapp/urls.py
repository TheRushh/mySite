from django.urls import include, re_path, path
from .views import *

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^about/$', about, name='about'),
    re_path(r'^category/(?P<cat_no>\d+)/$', detail, name='detail'),
    re_path(r'^products/$', products, name='products'),
    re_path(r'^placeorder/$', place_order, name='placeorder'),
    re_path(r'^products/(?P<prod_id>\d+)/$', productdetail, name='productdetail')
    # re_path(r'^contactus\d*/$', contact, name='contact'),
]
