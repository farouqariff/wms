from django.db import models


class PagePermissions(models.Model):
    """
    This model is only used to define custom permissions for pages.
    We don't actually store any data in this table.
    """
    class Meta:
        managed = False  # Don't create a table
        default_permissions = ()  # Remove default permissions
        permissions = [
            ('view_operator_page', 'Can view operator page'),
            ('view_manager_page', 'Can view manager page'),
        ]

