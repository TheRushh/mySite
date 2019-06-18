from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from myapp.models import Product
from .models import *
from .forms import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
import pandas as pd


# Create your views here.


def user_login(request):
    # print(request)
    # print(request.session)
    # print(request.session.keys())
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username, password)
        user = authenticate(username=username, password=password)
        # print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                dt = datetime.datetime.now()
                request.session['last_login'] = str(dt)
                request.session.set_expiry(3600)
                return HttpResponseRedirect(reverse('myapp:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')

    else:
        return render(request, 'myapp/login.html')


@login_required
def user_logout(request):
    logout(request)
    response = HttpResponseRedirect(reverse('myapp:index'))
    response.set_cookie('last_activity', str(datetime.datetime.now()))
    return response


def index(request):
    msg = ''
    flag = ''
    now = datetime.datetime.now()
    if 'last_login' in request.session.keys():
        last_login = pd.to_datetime(request.session.get('last_login'))
        flag = last_login
        msg = last_login
    elif 'last_activity' in request.COOKIES:
        last_activity = pd.to_datetime(request.COOKIES['last_activity'])
        flag = last_activity
        ago_hrs = (datetime.datetime.now()-last_activity).total_seconds()/3600
        if ago_hrs < 1:
            msg = last_activity
        else:
            msg = 'More than hour ago'
    else:
        msg = 'Last login more than one hour ago'
    cat_list = Category.objects.all().order_by('id')[:10]
    print(msg)
    response = render(request, 'myapp/index.html', {'cat_list': cat_list, 'msg': msg})
    response.set_cookie('last_activity', flag)
    print(request.COOKIES)
    return response
    # return render(request, 'index.html',{})


def about(request):
    msg = 'This is an Online Store App'
    # print(request.COOKIES)
    if 'visits' not in request.COOKIES:
        response = render(request, 'myapp/about.html', {'msg': msg, 'visits': 1})
        response.set_cookie('visits', 1)
    else:
        visits = int(request.COOKIES['visits'])
        visits += 1
        response = render(request, 'myapp/about.html', {'msg': msg, 'visits': visits})
        response.set_cookie('visits', visits)
    return response


def detail(request, cat_no):
    # catgory = Category.objects.get(pk=cat_no)
    category = get_object_or_404(Category, pk=cat_no)
    products = Product.objects.all().filter(category=category)
    # return response
    return render(request, 'myapp/detail.html', {'category': category, 'products': products})

# def handler404(request, exception, template_name="404.html"):
#     response = render_to_response("404.html")
#     response.status_code = 404
#     return response


def products(request):
    prod_list = Product.objects.all().order_by('id')[:10]
    return render(request, 'myapp/products.html', {'prod_list': prod_list})


def productdetail(request, prod_id):
    product: Product = Product.objects.get(pk=prod_id)
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            interested = form.cleaned_data['intersted']
            # print(interested)
            if interested == '1':
                product.interested += 1
                product.save()
            return redirect('myapp:index')
    else:
        form = InterestForm()
    return render(request, 'myapp/productdetail.html', {'product': product, 'form': form})


def place_order(request):
    msg = ''
    prod_list = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.num_units < order.product.stock:
                order.save()
                msg = 'Order Placed Successfully'
            else:
                msg = 'We do not have sufficient stock to fill your order'
            return render(request, 'myapp/order_response.html', {'msg': msg})
    else:
        form = OrderForm()
    return render(request, 'myapp/placeorder.html', {'form': form, 'msg': msg, 'prod_list':prod_list})


def myorders(request):
    user = request.user
    if user.is_authenticated:
        # print('myorder', user.username)
        client = Client.objects.get(username=user.username)
        if type(client) is Client:
            orders = Order.objects.filter(client=client)
            # print(orders)
            return render(request, 'myapp/myorders.html', {'orders': orders, 'client':client})

    else:
        return HttpResponse('You are not authenticated')
    return 0