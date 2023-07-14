
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .serializers import (VendorSerialiser, ProductCategorySerialiser, 
                          ProductSerializer, CustomerSerializer, OrderItemsSerializer, 
                          OrderSerializer, CustomerAddressSerializer)
from ecommapp.models import Vendor, Product_Category, Product, Customer, Order, OrderItems, CustomerAddress
from rest_framework.views import APIView


class GetVendors(generics.ListCreateAPIView):
    #def get(self,request):
        queryset= Vendor.objects.all()
        serializer_class= VendorSerialiser
        #return Response(serializer.data)
       

class GetVendorsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerialiser


class GetProductCategory(APIView):
    def get(self,request, *args, **kwargs):
        qs= Product_Category.objects.all()
        serializer= ProductCategorySerialiser(qs, many = True)
        return Response(serializer.data)

class GetProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product_Category.objects.all()
    serializer_class = ProductCategorySerialiser
    
class GetProduct(APIView):
    def get(self,request, *args, **kwargs):
        qs= Product.objects.all()
        serializer= ProductSerializer(qs, many = True)
        return Response(serializer.data)

class GetProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class GetCustomer (APIView):
    def get(self, request, *args, **kwargs):
        qs = Customer.objects.all()
        serializer = CustomerSerializer(qs, many = True)
        return Response(serializer.data)

class GetCustomerAddress(viewsets.ModelViewSet):
     queryset = CustomerAddress.objects.all()
     serializer_class = CustomerAddressSerializer
    
class GetCustomerDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class GetOrder (generics.ListCreateAPIView):
    #def get(self, request, *args, **kwargs):
        queryset = Order.objects.all()
        serializer_class = OrderSerializer
        #return Response(serializer.data)
    
class GetOrderDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
 
class GetOrderItems (generics.ListCreateAPIView):
    #def get(self, request, *args, **kwargs):
        queryset = OrderItems.objects.all()
        serializer_class = OrderItemsSerializer
        #return Response(serializer.data)
    
class GetOrderItemsDetail (APIView):
    def get(self, request, order_id):
       customer = Customer.objects.get(pk=order_id)
       order = Order.objects.get(customer = customer)
       qs = OrderItems.objects.filter(order = order)
       serializer = OrderItemsSerializer(qs, many = True)
       return Response (serializer.data)
    
    


