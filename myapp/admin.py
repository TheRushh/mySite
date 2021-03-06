from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Category)

admin.site.register(Order)


def restock(modeladmin, request, queryset):
    for product in queryset:
        product.stock = product.stock + 50
        product.save()
    return


restock.short_description = 'Update stock'


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'stock',
        'available',
        'interested',
        'description'
    )
    actions = [restock]


admin.site.register(Product, ProductAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'first_name',
        'last_name',
        'city',
        'get_interested'
    ]


admin.site.register(Client, ClientAdmin)
