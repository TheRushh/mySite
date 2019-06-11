from django.shortcuts import render, redirect, get_object_or_404, render_to_response

from myapp.models import Product
from .models import *
from .forms import *
from django.http import HttpResponse


# Create your views here.

def index(request):
    cat_list = Category.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html', {'cat_list': cat_list})
    # return render(request, 'index.html',{})


def about(request):
    msg = 'This is an Online Store App'
    return render(request, 'myapp/about.html', {'msg': msg})


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
    return render(request, 'myapp/products.html', {'prod_list':prod_list})

def productdetail(request, prod_id):
    product: Product = Product.objects.get(pk=prod_id)
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            interested = form.cleaned_data['intersted']
            print(interested)
            if interested == '1':
                product.interested += 1
                product.save()
            return redirect('index')
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
            return render(request, 'myapp/order_response.html', {'msg':msg})
    else:
        form = OrderForm()
    return render(request, 'myapp/placeorder.html', {'form':form, 'msg':msg, 'prod_list':prod_list})