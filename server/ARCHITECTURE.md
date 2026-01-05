# WMS Backend - Modular Architecture

## Project Structure

```
server/
├── core/                    # Core authentication and base models
├── warehouse/               # Warehouse management module
├── product/                 # Product, Category, Tag management
├── inventory/               # Inventory tracking module
├── user/                    # User profile extensions
├── role_permission/         # API access to Groups/Permissions
└── wms/                     # Django project settings
```

## Modules Overview

### 1. **Warehouse Module** (`warehouse/`)
Manages warehouse locations.

**Models:**
- `Warehouse` - Warehouse locations

**API Endpoints:** `/api/warehouses/`

---

### 2. **Product Module** (`product/`)
Manages products, categories, and tags.

**Models:**
- `Product` - Product information
- `Category` - Product categories
- `Tag` - Product tags
- `ProductTag` - Product-Tag relationships (through table)

**API Endpoints:**
- `/api/products/`
- `/api/categories/`
- `/api/tags/`
- `/api/product-tags/`

---

### 3. **Inventory Module** (`inventory/`)
Tracks product stock levels across warehouses.

**Models:**
- `Inventory` - Stock tracking per warehouse-product

**API Endpoints:** `/api/inventory/`

---

### 4. **User Module** (`user/`)
Extends Django's built-in User model with additional profile fields.

**Models:**
- `UserProfile` - Additional user fields (phone, etc.)

**Uses Django's built-in:** `django.contrib.auth.models.User`

**API Endpoints:** `/api/users/`

---

### 5. **Role & Permission Module** (`role_permission/`)
Provides API access to Django's built-in Group and Permission models.

**Uses Django's built-in:**
- `django.contrib.auth.models.Group` (acts as Roles)
- `django.contrib.auth.models.Permission`

**API Endpoints:**
- `/api/groups/` - Manage user groups (roles)
- `/api/permissions/` - View available permissions

---

## Authentication System

Uses **Django's built-in authentication**:
- **User Model**: `django.contrib.auth.models.User`
- **Groups as Roles**: Use Django's `Group` model for role-based access
- **Permissions**: Use Django's `Permission` model
- **UserProfile**: OneToOne extension for custom fields

### Example Role Setup:
```python
from django.contrib.auth.models import Group, Permission

# Create roles
admin_group = Group.objects.create(name='Admin')
manager_group = Group.objects.create(name='Manager')
operator_group = Group.objects.create(name='Operator')

# Assign permissions
admin_group.permissions.add(*Permission.objects.all())
```

---

## Module Structure Template

Each module follows this structure:
```
module_name/
├── __init__.py
├── models.py           # Database models
├── views.py            # ViewSets (API views)
├── serializers.py      # DRF serializers
├── urls.py             # URL routing
├── admin.py            # Django admin config
├── tests.py            # Unit tests
└── migrations/         # Database migrations
```

---

## API Overview

All endpoints require authentication.

| Module | Endpoint | Description |
|--------|----------|-------------|
| Warehouse | `/api/warehouses/` | Warehouse CRUD |
| Product | `/api/products/` | Product CRUD |
| Product | `/api/categories/` | Category CRUD |
| Product | `/api/tags/` | Tag CRUD |
| Inventory | `/api/inventory/` | Inventory CRUD |
| User | `/api/users/` | User management |
| Role/Permission | `/api/groups/` | Role (Group) management |
| Role/Permission | `/api/permissions/` | Permission viewing |

---

## Database Tables

| Table | Module | Description |
|-------|--------|-------------|
| `warehouse` | warehouse | Warehouse locations |
| `category` | product | Product categories |
| `tag` | product | Product tags |
| `product` | product | Products |
| `producttag` | product | Product-tag relationships |
| `inventory` | product/inventory | Stock levels |
| `user_profile` | user | Extended user info |
| `auth_user` | Django built-in | Users |
| `auth_group` | Django built-in | Roles (Groups) |
| `auth_permission` | Django built-in | Permissions |

---

## Benefits of This Architecture

✅ **Modular**: Each domain has its own app
✅ **Scalable**: Easy to add new modules
✅ **Maintainable**: Clear separation of concerns
✅ **Reusable**: Modules can be extracted/reused
✅ **Standard**: Follows Django best practices
✅ **Simple Auth**: Uses battle-tested Django auth system
