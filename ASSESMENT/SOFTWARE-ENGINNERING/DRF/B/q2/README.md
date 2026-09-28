# MenuItem CRUD REST API

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

## Endpoints

GET all:
`GET /api/menu-items/`

Create:
`POST /api/menu-items/`

Retrieve:
`GET /api/menu-items/<id>/`

Update:
`PUT /api/menu-items/<id>/`

Delete:
`DELETE /api/menu-items/<id>/`

Category list:
`GET /api/categories/`

## Create example

```json
{
    "name": "Margherita Pizza",
    "price": "299.00",
    "category": 1,
    "is_available": true
}
```

Successful creation returns HTTP 201.

Invalid price:

```json
{
    "name": "Invalid Item",
    "price": "0",
    "category": 1,
    "is_available": true
}
```

returns HTTP 400 with a validation error.

A missing MenuItem ID returns HTTP 404.
