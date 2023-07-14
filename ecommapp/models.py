from django.db import models
from django.contrib.auth.models import User


# Vendor

class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)

    def __str__(self):
       return self.user.username
    
    
#product_category

class Product_Category(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)

    def __str__(self):
        return self.title
    
    
#product model

class Product(models.Model):
    category = models.ForeignKey(Product_Category, on_delete=models.SET_NULL, null=True, related_name='category_product')
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

class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name ='customer_address')
    address = models.TextField()
    default_address = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.user.username


# Order models

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.user.username


    
# order Items model

class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items' )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
       return self.product.product_title
    

# Product Rating 

class ProductRating(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_ratings')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_rating')
    rating = models.IntegerField()
    review = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review