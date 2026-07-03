# Django Company APIs

A Django REST API project that provides endpoints to:

- Retrieve the list of companies
- Retrieve company executives using company IDs

---

# Features

- RESTful API implementation
- Company listing endpoint
- Company executives endpoint
- JSON responses
- Django + Django REST Framework based architecture

---

# API Endpoints

## 1. Get Companies List

Returns the list of all companies.

### Endpoint

```http
GET /api/companies/
```

### Sample Response

```json
[
  {
    "id": 1,
    "name": "ABC Corp"
  },
  {
    "id": 2,
    "name": "XYZ Ltd"
  }
]
```

---

## 2. Get Company Executives

Returns executives for the provided company IDs.

### Endpoint

```http
POST /company-executives/
```

### Request Body

```json
{
  "company_ids": [1, 2]
}
```

### Sample Response

```json
[
  {
    "company_id": 1,
    "executives": [
      {
        "name": "John Doe",
        "designation": "CEO"
      }
    ]
  }
]
```

---

# Tech Stack

- Python
- Django
- Django REST Framework

---



# Author

Developed as part of a Django API task project.
