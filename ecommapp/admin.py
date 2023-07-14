from django.contrib import admin
from .models import Vendor, Product_Category, Product, Customer, Order, OrderItems, CustomerAddress

admin.site.register([Vendor, Product_Category, Product, Customer, Order, OrderItems, CustomerAddress])
