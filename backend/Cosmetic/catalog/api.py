from rest_framework import viewsets, permissions

from catalog.serializers import *
from catalog.models import *


class ProductsViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductsSerializer