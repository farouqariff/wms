from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group, Permission
from .serializers import GroupSerializer, PermissionSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """ViewSet for managing groups (roles)"""
    queryset = Group.objects.prefetch_related('permissions').all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing permissions (read-only)"""
    queryset = Permission.objects.select_related('content_type').all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]
