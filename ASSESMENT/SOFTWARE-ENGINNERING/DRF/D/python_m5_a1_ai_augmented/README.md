# Python M5-A1 — AI-Augmented Learning

## STEP 1 — BUILD WITH AI

This project implements:

`POST /api/orders/place/`

Request body:
```json
{
  "customer_name": "Parth",
  "item": "Pizza",
  "quantity": 2
}
```

The endpoint:
- accepts customer_name, item, quantity
- validates quantity as a positive integer
- returns HTTP 400 with a JSON error when validation fails
- saves a valid order to SQLite
- returns the saved order including auto-generated id
- returns HTTP 201 on success

## STEP 2 — TEST & DEBUG WITHOUT AI

Suggested manual test:
1. Send a valid request with quantity `2`.
2. Send an invalid request with quantity `0`.
3. Send an invalid request with quantity `-1`.
4. Send an invalid request with a non-integer quantity such as `"two"`.

### Example validation improvement

The initial AI-style implementation can be improved by validating `customer_name` and `item` as non-empty values, not only quantity. The final serializer below performs those validations too.

## Postman screenshots

Add:
1. Successful POST request — HTTP 201
2. Validation failure — HTTP 400

## Run

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

URL:

`POST http://127.0.0.1:8000/api/orders/place/`
