# Food Delivery REST API Backend

A Django REST Framework backend for a food delivery platform.

## Features
- Category CRUD using ModelSerializer + ModelViewSet
- MenuItem CRUD using ModelSerializer + ModelViewSet
- Order CRUD using ModelSerializer + ModelViewSet
- DefaultRouter
- TokenAuthentication
- IsAuthenticated protection for Order endpoints
- PageNumberPagination with page_size = 5
- Order status filtering
- Serializer field validation
- Django Admin

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Create a token from Django admin or shell:

```bash
python manage.py drf_create_token <username>
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /api/categories/ | List categories |
| POST | /api/categories/ | Create category |
| GET | /api/categories/{id}/ | Category detail |
| PUT/PATCH | /api/categories/{id}/ | Update category |
| DELETE | /api/categories/{id}/ | Delete category |
| GET | /api/menuitems/ | List menu items |
| POST | /api/menuitems/ | Create menu item |
| GET | /api/menuitems/{id}/ | Menu item detail |
| PUT/PATCH | /api/menuitems/{id}/ | Update menu item |
| DELETE | /api/menuitems/{id}/ | Delete menu item |
| GET | /api/orders/ | Authenticated order history |
| POST | /api/orders/ | Authenticated order creation |
| GET | /api/orders/{id}/ | Order detail |
| PUT/PATCH | /api/orders/{id}/ | Update order |
| DELETE | /api/orders/{id}/ | Delete order |

## Authentication

Use this header for Order endpoints:

`Authorization: Token YOUR_TOKEN`

Unauthenticated Order requests return HTTP 401.

## Order filtering

Example:

`GET /api/orders/?status=Pending`

## Pagination

Order listing uses PageNumberPagination with:

`page_size = 5`

## Postman Screenshots

Add your Postman screenshots here before submission.
