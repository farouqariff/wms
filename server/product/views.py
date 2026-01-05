from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product, Category, Tag, ProductTag
from .serializers import ProductSerializer, CategorySerializer, TagSerializer, ProductTagSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for managing products"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['category', 'is_archived']
    search_fields = ['name', 'sku']


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for managing categories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class TagViewSet(viewsets.ModelViewSet):
    """ViewSet for managing tags"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class ProductTagViewSet(viewsets.ModelViewSet):
    """ViewSet for managing product-tag relationships"""
    queryset = ProductTag.objects.all()
    serializer_class = ProductTagSerializer
    permission_classes = [IsAuthenticated]
