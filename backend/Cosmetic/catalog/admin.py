from django.contrib import admin

from catalog.models import *


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):

    list_display = ('id', 'title_of_product','type_of_product', 'price')
    search_fields = ('id', 'title_of_product', 'type_of_product')
    list_filter = ('id', 'price')
