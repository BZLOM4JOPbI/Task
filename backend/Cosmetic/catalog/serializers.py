from rest_framework import serializers

from catalog.models import *


class CreamsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Creams
        fields = ['brand', 'title_of_product', 'brief_info_about_product', 'description', 'price']
