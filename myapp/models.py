from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    warehouse = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    interested = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=200, blank=True)

    def refill(self):
        self.stock += 100

    def __str__(self):
        return "{name} (Stock: {stock})".format(name=self.name, stock=self.stock)

    def __unicode__(self):
        return "%s" % self.name


class Client(User):
    PROVINCES_CHOICES = [
        ('AB', 'Alberta'),
        ('MB', 'Manitoba'),
        ('ON', 'Ontario'),
        ('QC', 'Quebec')
    ]
    company = models.CharField(max_length=50, null=True)
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=2, choices=PROVINCES_CHOICES, default='ON')
    interested_in = models.ManyToManyField(Category)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Order(models.Model):
    ORDER_STATUS = [
        (0, 'Order Cancelled'),
        (1, 'Order Placed'),
        (2, 'Order Shipped'),
        (3, 'Oder Delivered')
    ]
    product = models.ForeignKey(Product, related_name='product', on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, related_name='client', on_delete=models.DO_NOTHING)
    num_units = models.PositiveIntegerField(default=1)
    order_status = models.IntegerField(choices=ORDER_STATUS, default='1')
    status_date = models.DateField(default=timezone.now)

    def __str__(self):
        return "%s %s for %s %s" % (self.num_units, self.product, self.client.first_name, self.client.last_name)

    def __unicode__(self):
        return "%s %s %s for %s %s" % (self.pk, self.num_units, self.product, self.client.first_name, self.client.last_name)

    def total_cost(self):
        return "%d" % (self.num_units * self.product.price)
