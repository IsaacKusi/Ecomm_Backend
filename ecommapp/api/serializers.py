
from rest_framework.serializers import ModelSerializer
from ecommapp.models import Vendor, Product_Category


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
        fields = ['product_title', 'product_detail']


