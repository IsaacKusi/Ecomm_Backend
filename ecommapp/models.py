from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)

    def __str__(self):
       return self.user.username



class Product_Category(models.Model):
    product_title = models.CharField(max_length=200)
    product_detail = models.TextField(null=True)

    def __str__(self):
        return self.product_title

class Product(models.Model):
    product_title = models.CharField(max_length=200)
    product_detail = models.TextField(null=True)
    price = models.FloatField()

    def __str__(self):
        return self.product_title



