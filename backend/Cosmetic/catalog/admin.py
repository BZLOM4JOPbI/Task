from django.contrib import admin

from catalog.models import *


@admin.register(Creams)
class CreamsAdmin(admin.ModelAdmin):

    list_display = ('id', 'title_of_product','type_of_derm', 'price')
    search_fields = ('id', 'title_of_product', 'type_of_derm')
    list_filter = ('id', 'price')
