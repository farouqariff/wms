from django.db import models


class Category(models.Model):
    """Product category model"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'categories'


class Tag(models.Model):
    """Product tag model"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'


class Product(models.Model):
    """Product model"""
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField(blank=True, null=True)
    low_stock_threshold = models.IntegerField(default=0)
    is_archived = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, through='ProductTag', related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'


class ProductTag(models.Model):
    """Product-Tag relationship model"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'producttag'
        unique_together = ('product', 'tag')
