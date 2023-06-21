
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import VendorSerialiser, ProductCategorySerialiser
from ecommapp.models import Vendor, Product_Category
from rest_framework.views import APIView



class GetVendors(APIView):
    #permission_classes = (IsAuthenticated, )
    def post(self,request, *args, **kwargs):
        qs= Vendor.objects.all()
        serializer= VendorSerialiser(qs, many=True)
        return Response(serializer.data)

class GetProductCategory(APIView):
    # permission_classes = (IsAuthenticated, )
    def post(self,request, *args, **kwargs):
        #qs= Product_Category.objects.all()
        serializer= ProductCategorySerialiser(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
