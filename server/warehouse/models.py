from django.db import models


class Warehouse(models.Model):
    """Warehouse location model"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'warehouse'

