from django.contrib import admin
from .models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'warehouse', 'product', 'stock']
    list_filter = ['warehouse']
    search_fields = ['product__name', 'warehouse__name']
