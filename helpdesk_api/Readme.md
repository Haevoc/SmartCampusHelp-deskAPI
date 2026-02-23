# Smart Campus Helpdesk API

A RESTful backend system where students can raise campus issues (tickets) and administrators can manage them.

Built using **Django + Django REST Framework + PostgreSQL + JWT Authentication**

---

## Features

* Ticket CRUD operations
* JWT based authentication
* Admin session login support
* Pagination
* Filtering by category & status
* Ordering by priority & created date
* Search by title & description
* Secure protected endpoints

---

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* SimpleJWT

---

## Authentication Flow

1. User logs in using username & password
2. Server returns access and refresh tokens
3. Access token must be sent in Authorization header

```
Authorization: Bearer <access_token>
```

---

## API Endpoints

### Authentication

| Method | Endpoint            | Description          |
| ------ | ------------------- | -------------------- |
| POST   | /api/token/         | Login & get tokens   |

---

### Tickets

| Method | Endpoint       | Description          |
| ------ | -------------- | -------------------- |
| POST   | /tickets/      | Create ticket        |
| GET    | /tickets/      | List tickets         |
| GET    | /tickets/<id>/ | Ticket details       |
| PATCH  | /tickets/<id>/ | Update ticket status |
| DELETE | /tickets/<id>/ | Delete ticket        |

---

## Ticket Fields

| Field       | Type                         | Description         |
| ----------- | ---------------------------- | ------------------- |
| title       | string                       | Issue title         |
| description | text                         | Issue details       |
| category    | classroom / hostel / network | Issue location type |
| priority    | low / medium / high          | Urgency level       |
| status      | open / in-progress / closed  | Ticket progress     |
| created_at  | datetime                     | Created time        |
| updated_at  | datetime                     | Last updated time   |

---

## Filtering

```
/tickets/?category=network
/tickets/?status=open
```

---

## Searching

```
/tickets/?search=wifi
```

---

## Ordering

```
/tickets/?ordering=priority
/tickets/?ordering=-created_at
```

---

## Pagination

```
/tickets/?page=2
```

---

## Example Request

Create Ticket

```
POST /tickets/
Content-Type: application/json
Authorization: Bearer <token>

{
  "title": "WiFi not working",
  "description": "No internet in block A",
  "category": "network",
  "priority": "high"
}
```

---

## Database

PostgreSQL is used as the primary database.

Configure in settings.py:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}
```

---

## Setup Instructions

1. Clone repository

```
git clone <repo-url>
cd helpdesk
```

2. Create virtual environment

```
python -m venv env
env\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Apply migrations

```
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser

```
python manage.py createsuperuser
```

6. Run server

```
python manage.py runserver
```

---

## Testing

Use Postman or any REST client.

Login → Copy access token → Call protected APIs.

---

## Future Improvements

* User based ticket ownership
* Role based permissions
* Redis caching for ticket list
* Email notifications

---

