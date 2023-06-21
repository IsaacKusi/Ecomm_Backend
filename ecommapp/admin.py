from django.contrib import admin
from .models import Vendor, Product_Category, Product

admin.site.register([Vendor, Product_Category, Product])
