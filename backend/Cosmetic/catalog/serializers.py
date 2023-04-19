from rest_framework import serializers

from catalog.models import Creams


class CreamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creams
        fields = [
            "brand",
            "title_of_product",
            "short_description",
            "description",
            "price",
        ]
