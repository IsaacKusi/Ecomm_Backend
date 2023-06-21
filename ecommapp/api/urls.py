
from django.urls import path
from .views import GetVendors, GetProductCategory

urlpatterns = [
    path('vendors', GetVendors.as_view(), name='vendor'),
    path('product_categories', GetProductCategory.as_view(), name='category'),
]