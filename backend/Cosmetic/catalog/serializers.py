from rest_framework import serializers

from catalog.models import *


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Products
        fields = ['title_of_product', 'type_of_product', 'price']
