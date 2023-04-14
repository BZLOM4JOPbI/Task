from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from catalog.serializers import *
from catalog.models import *


# class ProductsViewSet(viewsets.ModelViewSet):

#     queryset = Products.objects.all()
#     permissions_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = ProductsSerializer


class ProductsAPiView(APIView):

    def get(self, request):
        
        filters = request.query_params
        print(filters)
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)

        return Response({'data': serializer.data})

    def post(self, request):

        new_product = request.data
        print(new_product)
        serializer = ProductsSerializer(data=new_product)

        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({'Success': f'Товар {product_saved.title_of_product} успешно добавлен'})
