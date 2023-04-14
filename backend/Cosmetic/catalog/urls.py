from django.urls import path
from rest_framework import routers

from catalog.api import *


# router = routers.DefaultRouter()
# router.register('api/products', ProductsViewSet, 'products')


# urlpatterns = router.urls


urlpatterns = [
    path('api/products/', ProductsAPiView.as_view())
]