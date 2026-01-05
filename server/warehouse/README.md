# Warehouse Module

This is a modular Django app for managing warehouse locations.

## Structure

```
warehouse/
├── __init__.py
├── admin.py          # Django admin configuration
├── apps.py           # App configuration
├── models.py         # Warehouse model
├── serializers.py    # DRF serializers
├── views.py          # ViewSets and API views
├── urls.py           # URL routing
├── tests.py          # Unit tests
└── migrations/       # Database migrations
```

## Model

**Warehouse**

- `id`: Auto-generated primary key
- `name`: Warehouse name (CharField, max 255)

## API Endpoints

Base URL: `/api/warehouses/`

- `GET /api/warehouses/` - List all warehouses
- `POST /api/warehouses/` - Create a new warehouse
- `GET /api/warehouses/{id}/` - Retrieve a specific warehouse
- `PUT /api/warehouses/{id}/` - Update a warehouse
- `PATCH /api/warehouses/{id}/` - Partial update
- `DELETE /api/warehouses/{id}/` - Delete a warehouse

## Usage

All endpoints require authentication.

Example request:

```json
POST /api/warehouses/
{
    "name": "Main Warehouse"
}
```
