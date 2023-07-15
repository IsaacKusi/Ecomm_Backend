
from rest_framework.serializers import ModelSerializer
from ecommapp.models import (Vendor, Product_Category, Product, Customer, 
                             Order, OrderItems, CustomerAddress, ProductRating)


class VendorSerialiser(ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('__all__')
    
    def __init__(self, *args, **kwargs):
        super(VendorSerialiser,self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class ProductCategorySerialiser(ModelSerializer):
    class Meta:
        model = Product_Category
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(ProductCategorySerialiser,self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(ProductSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')

    def  __init__(self,*args, **kwargs):
        super(CustomerSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class CustomerAddressSerializer(ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = ('__all__')

    def  __init__(self,*args, **kwargs):
        super(CustomerAddressSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class OrderSerializer (ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')
    
    def __init__(self, *args, **kwargs):
        super(OrderSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1  

class OrderItemsSerializer (ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(OrderItemsSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1   

class ProductRatingSerializer (ModelSerializer):
    class Meta:
        model = ProductRating
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(ProductRatingSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1   

