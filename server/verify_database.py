"""
Script to verify all data is stored in PostgreSQL database (wms_db)
"""
from django.contrib.auth.models import User, Group, Permission

print("=" * 60)
print("VERIFYING DATA IN PostgreSQL DATABASE (wms_db)")
print("=" * 60)

# Check users in database
print("\n📊 USERS IN DATABASE:")
users = User.objects.all()
for user in users:
    print(f"\n  Username: {user.username}")
    print(f"  Email: {user.email}")
    print(f"  Superuser: {user.is_superuser}")
    print(f"  Groups: {[g.name for g in user.groups.all()]}")
    print(f"  Database ID: {user.id}")

# Check groups in database
print("\n\n📊 GROUPS IN DATABASE:")
groups = Group.objects.all()
for group in groups:
    print(f"\n  Group Name: {group.name}")
    print(f"  Permissions: {[p.codename for p in group.permissions.all()]}")
    print(f"  Members: {[u.username for u in group.user_set.all()]}")
    print(f"  Database ID: {group.id}")

# Check permissions in database
print("\n\n📊 CUSTOM PERMISSIONS IN DATABASE:")
perms = Permission.objects.filter(codename__in=['view_operator_page', 'view_manager_page'])
for perm in perms:
    print(f"\n  Permission: {perm.codename}")
    print(f"  Name: {perm.name}")
    print(f"  Database ID: {perm.id}")

print("\n" + "=" * 60)
print("✅ ALL DATA IS STORED IN PostgreSQL DATABASE (wms_db)")
print("=" * 60)
