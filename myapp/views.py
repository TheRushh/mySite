from django.shortcuts import render, get_object_or_404, render_to_response
from .models import *
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
