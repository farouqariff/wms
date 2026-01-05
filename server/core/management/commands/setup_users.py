from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from core.models import PagePermissions


class Command(BaseCommand):
    help = 'Setup users, groups, and permissions for the WMS system'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting setup...'))
        
        # Get or create permissions
        content_type = ContentType.objects.get_for_model(PagePermissions)
        view_operator_perm, _ = Permission.objects.get_or_create(
            codename='view_operator_page',
            name='Can view operator page',
            content_type=content_type,
        )
        view_manager_perm, _ = Permission.objects.get_or_create(
            codename='view_manager_page',
            name='Can view manager page',
            content_type=content_type,
        )
        self.stdout.write(self.style.SUCCESS('✓ Permissions created'))
        
        # Create groups
        operator_group, created = Group.objects.get_or_create(name='operator')
        if created:
            operator_group.permissions.add(view_operator_perm)
            self.stdout.write(self.style.SUCCESS('✓ Operator group created'))
        else:
            self.stdout.write(self.style.WARNING('⚠ Operator group already exists'))
        
        manager_group, created = Group.objects.get_or_create(name='manager')
        if created:
            manager_group.permissions.add(view_manager_perm)
            self.stdout.write(self.style.SUCCESS('✓ Manager group created'))
        else:
            self.stdout.write(self.style.WARNING('⚠ Manager group already exists'))
        
        # Create users
        # 1. Admin (superuser)
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@wms.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('✓ Admin user created (username: admin, password: admin123)'))
        else:
            self.stdout.write(self.style.WARNING('⚠ Admin user already exists'))
        
        # 2. Manager user
        if not User.objects.filter(username='manager').exists():
            manager_user = User.objects.create_user(
                username='manager',
                email='manager@wms.com',
                password='manager123'
            )
            manager_user.groups.add(manager_group)
            self.stdout.write(self.style.SUCCESS('✓ Manager user created (username: manager, password: manager123)'))
        else:
            self.stdout.write(self.style.WARNING('⚠ Manager user already exists'))
        
        # 3. Operator user
        if not User.objects.filter(username='operator').exists():
            operator_user = User.objects.create_user(
                username='operator',
                email='operator@wms.com',
                password='operator123'
            )
            operator_user.groups.add(operator_group)
            self.stdout.write(self.style.SUCCESS('✓ Operator user created (username: operator, password: operator123)'))
        else:
            self.stdout.write(self.style.WARNING('⚠ Operator user already exists'))
        
        self.stdout.write(self.style.SUCCESS('\n=== Setup Complete! ==='))
        self.stdout.write(self.style.SUCCESS('\nTest Credentials:'))
        self.stdout.write('1. Admin    - username: admin    | password: admin123    (Access: All pages)')
        self.stdout.write('2. Manager  - username: manager  | password: manager123  (Access: Manager page only)')
        self.stdout.write('3. Operator - username: operator | password: operator123 (Access: Operator page only)')
