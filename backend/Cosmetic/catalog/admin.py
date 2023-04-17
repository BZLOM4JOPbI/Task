from django.contrib import admin

from catalog.models import *


@admin.register(Creams)
class CreamsAdmin(admin.ModelAdmin):

    list_display = ('id', 'brand', 'title_of_product','brief_info_about_product', 'price')
    search_fields = ('id', 'brand', 'title_of_product')
    list_filter = ('id', 'price')
