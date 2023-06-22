
from rest_framework.response import Response
from rest_framework import generics
from .serializers import VendorSerialiser, ProductCategorySerialiser, ProductSerializer
from ecommapp.models import Vendor, Product_Category, Product
from rest_framework.views import APIView


class GetVendors(APIView):
    def get(self,request, *args, **kwargs):
        qs= Vendor.objects.all()
        serializer= VendorSerialiser(qs, many=True)
        return Response(serializer.data)

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
