from django.contrib import admin

from catalog.models import Creams


@admin.register(Creams)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "brand",
        "title_of_product",
        "short_description",
        'isHit',
        "price",
        'sale',
    )

    search_fields = ("id", "brand", "title_of_product", 'isHit')

    list_filter = ("id", "price", 'sale')
