from django.shortcuts import render, get_object_or_404, render_to_response
from .models import *
from django.http import HttpResponse
from django.conf.urls import handler404



# Create your views here.

def index(request):
    cat_list = Category.objects.all().order_by('id')[:10]
    prod_list = Product.objects.all().order_by('-price')[:10]
    response = HttpResponse()
    heading1 = '<p>' + 'List of categories: ' + '</p>'
    heading2 = '<p>' + 'List of Products based on price: ' + '</p>'
    response.write(heading1)
    for category in cat_list:
        para = '<p>' + str(category.id) + ': ' + str(category) + '</p>'
        response.write(para)
    response.write(heading2)
    for products in prod_list:
        para = '<p>' + str(products) + ' Price=$' + str(products.price) + '</p>'
        response.write(para)
    return response
    # return render(request, 'index.html',{})


def about(request):
    response = HttpResponse()
    response.write('<h2>This is an Online Store App</h2>')
    return response


def detail(request, cat_no):
    print(cat_no)
    response = HttpResponse()
    category = get_object_or_404(Category, pk=cat_no)
    response.write(
        '<p>Warehouse for <b>{cat}</b> is at <b>{warehouse}</b></p>'.format(cat=category, warehouse=category.warehouse))
    products = Product.objects.all().filter(category=category)
    response.write('<p><b>Products are:</b></p>')
    response.write('<ul>')
    for __ in products:
        response.write('<li>{products}</li>'.format(products=__))
    return response


# def error_404(request):
#     data = {}
#     return render(request, 'myapp/error_404.htm;', data)


# def contact(request):
#     priyal = HttpResponse()
#     myhtml1 = '<h2>Contact Us info</h2>'
#     priyal.write(myhtml1)
#     myhtml2 = '<p>My Number is 2269751892</p>'
#     priyal.write(myhtml2)
#     return priyal

def handler404(request, exception, template_name="error_404.html"):
    response = render_to_response("error_404.html")
    response.status_code = 404
    return response

# def test(request):
#     return render(request, 'index.html',{})