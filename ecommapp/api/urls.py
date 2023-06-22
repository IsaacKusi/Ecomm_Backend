
from django.urls import path
from .views import (GetVendors, GetProductCategory, GetProduct, 
                    GetVendorsDetail,GetProductCategoryDetail, GetProductDetail)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('vendors', GetVendors.as_view(), name='vendor'),
    path('vendor/details/<int:pk>', GetVendorsDetail.as_view(), name='vendor'),
    path('product_categories', GetProductCategory.as_view(), name='category'),
    path('product_categorie/details/<int:pk>', GetProductCategoryDetail.as_view(), name='category'),
    path('products', GetProduct.as_view(), name='product'),
    path('product/details/<int:pk>', GetProductDetail.as_view(), name='product'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]