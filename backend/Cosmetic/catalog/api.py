from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from catalog.serializers import *
from catalog.models import *
from catalog.utils import *


class CreamsAPiView(APIView):

    def get(self, request):
        
        filter_type_of_derm, filter_brand, filter_cream_for = get_filters_from_request(request)

        creams = Creams.objects.filter(
            brand__in=filter_brand,
            type_of_derm__in=filter_type_of_derm,
            cream_for__in=filter_cream_for,
        )
        
        serializer = CreamsSerializer(creams, many=True)

        return Response({'data': serializer.data})

    def post(self, request):

        new_product = request.data
        serializer = CreamsSerializer(data=new_product)

        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()

        return Response({'Success': f'Товар {product_saved.title_of_product} успешно добавлен'})
