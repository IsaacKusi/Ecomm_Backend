
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (GetVendors, GetProductCategory, GetProduct, 
                    GetVendorsDetail,GetProductCategoryDetail, GetCustomer, 
                    GetProductDetail, GetCustomerDetail, GetOrder, GetOrderDetail,
                      GetOrderItems, GetOrderItemsDetail, GetCustomerAddress, GetProductRating,
                      GetProductRatingDetail)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('customer_addresses', GetCustomerAddress)
router.register('product_ratings', GetProductRating)

urlpatterns = [
    #vendors
    path('vendors', GetVendors.as_view(), name='vendor'),
    path('vendor/details/<int:pk>', GetVendorsDetail.as_view(), name='vendor'),

    #product categories
    path('product_categories', GetProductCategory.as_view(), name='category'),
    path('product_categorie/details/<int:pk>', GetProductCategoryDetail.as_view(), name='category_detail'),

    #products
    path('products', GetProduct.as_view(), name='product'),
    path('product/details/<int:pk>', GetProductDetail.as_view(), name='product'),

    #customers
    path('customers', GetCustomer.as_view(), name='customer'),
    path('customer/details/<int:pk>', GetCustomerDetail.as_view(), name='customer_detail'),

    #order
    path('orders', GetOrder.as_view(), name='order'),
    path('order/details/<int:pk>', GetOrderDetail.as_view(), name='order_detail'),

    #orderItems
    path('orderItems', GetOrderItems.as_view(), name='orderItem'),
    path('orderItems/details/<int:order_id>', GetOrderItemsDetail.as_view(), name='orderItems_detail'),

    #productRating
    path('rating/detail/<int:customer_id>', GetProductRatingDetail.as_view(), name='rating_detail'),

    #jwt tokens
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls