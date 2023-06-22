from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)

    def __str__(self):
       return self.user.username
    

class Product_Category(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Product_Category, on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    product_title = models.CharField(max_length=200)
    product_detail = models.TextField(null=True)
    price = models.FloatField()

    def __str__(self):
        return self.product_title


#customer models

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_number = models.PositiveBigIntegerField()

    def __str__(self):
       return self.user.username


# Order models

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
    

class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
       return self.product.product_title

