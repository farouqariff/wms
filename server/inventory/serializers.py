from rest_framework import serializers
from .models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    warehouse_name = serializers.CharField(source='warehouse.name', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_sku = serializers.CharField(source='product.sku', read_only=True)

    class Meta:
        model = Inventory
        fields = ['id', 'warehouse', 'warehouse_name', 'product', 'product_name', 
                  'product_sku', 'stock']
