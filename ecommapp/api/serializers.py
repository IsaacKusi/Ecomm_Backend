
from rest_framework.serializers import ModelSerializer
from ecommapp.models import Vendor, Product_Category, Product


class VendorSerialiser(ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('__all__')
    
    def __init__(self, *args, **kwargs):
        super(VendorSerialiser,self).__init__(*args, **kwargs)
        # self.Meta.depth = 1

class ProductCategorySerialiser(ModelSerializer):
    class Meta:
        model = Product_Category
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(ProductCategorySerialiser,self).__init__(*args, **kwargs)
        # self.Meta.depth = 1


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(ProductSerializer,self).__init__(*args, **kwargs)
        # self.Meta.depth = 1