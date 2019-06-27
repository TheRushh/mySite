from django.urls import include, re_path, path
from .views import *

app_name = 'myapp'

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^about/$', about, name='about'),
    re_path(r'^category/(?P<cat_no>\d+)/$', detail, name='detail'),
    re_path(r'^products/$', products, name='products'),
    re_path(r'^placeorder/$', place_order, name='placeorder'),
    re_path(r'^products/(?P<prod_id>\d+)/$', productdetail, name='productdetail'),
    re_path(r'^signup/$', user_signup, name='user_signup'),
    re_path(r'^login/', user_login, name='user_login'),
    re_path(r'^logout/$', user_logout, name='user_logout'),
    re_path(r'^myorders/$', myorders, name='myorders'),
    # re_path(r'^contactus\d*/$', contact, name='contact'),
]
