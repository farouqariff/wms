from django.db import models


class Inventory(models.Model):
    """Inventory tracking model"""
    warehouse = models.ForeignKey('warehouse.Warehouse', on_delete=models.CASCADE, related_name='inventory')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='inventory')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} at {self.warehouse.name}: {self.stock}"

    class Meta:
        db_table = 'inventory'
        unique_together = ('warehouse', 'product')
        verbose_name_plural = 'inventories'
