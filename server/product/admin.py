from django.contrib import admin
from .models import Product, Category, Tag, ProductTag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


class ProductTagInline(admin.TabularInline):
    model = ProductTag
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sku', 'category', 'unit_cost', 'is_archived']
    list_filter = ['category', 'is_archived']
    search_fields = ['name', 'sku']
    inlines = [ProductTagInline]


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'tag']
    list_filter = ['tag']
