# 📘 ALX Travel App 0x00

## **Models, Serializers, and Database Seeding**

This project is a continuation of the **ALX Pro Backend Engineering** training. In this milestone, we implement:

* Django database models
* DRF serializers
* A custom management command to seed the database
* PostgreSQL setup (Docker)

This README provides setup instructions, project structure, and how to run all required components.

---

# 🚀 **Project Overview**

This milestone focuses on creating the fundamental backend components of the **ALX Travel App**. You will:

### ✅ Define database models in Django

* `Listing`
* `Booking`
* `Review`

### ✅ Create API serializers

* `ListingSerializer`
* `BookingSerializer`
* `ReviewSerializer`

### ✅ Populate the database with sample data using a seeding script

* Custom management command: `python manage.py seed`

---

# 🛠 **Project Structure**

```
alx_travel_app_0x00/
│
├── manage.py
|
├── requirements.txt
│
├── alx_travel_app/
│   ├── manage.py  ← ✔ use THIS manage.py
│   └── alx_travel_app/
│       ├── settings.py
│       ├── urls.py
│       ├── wsgi.py
│       ├── asgi.py
│       └── listings/
│           ├── models.py
│           ├── serializers.py
│           ├── admin.py
│           ├── management/
│           │   └── commands/
│           │       └── seed.py
│           └── migrations/
└── docker-compose.yml
```

---

# 🐍 **Virtual Environment Setup**

```
cd alx_travel_app_0x00
python3 -m venv alx_travel_app_0x00_venv
source alx_travel_app_0x00_venv/bin/activate
```

Install dependencies:

```
pip install -r alx_travel_app/requirements.txt
```

---

# 🐘 **PostgreSQL Setup (Docker)**

Ensure your `docker-compose.yml` contains:

```yaml
services:
  db:
    image: postgres:16
    container_name: alxtravel_postgres
    environment:
      POSTGRES_DB: alxtravel
      POSTGRES_USER: alxuser
      POSTGRES_PASSWORD: alxpass
    ports:
      - "5433:5432"
    volumes:
      - db_data:/var/lib/postgresql/data
volumes:
  db_data:
```

Start Postgres:

```bash
docker compose up -d
```

---

# ⚙️ **Environment Variables**

Create a `.env` file inside:

```
alx_travel_app_0x00/alx_travel_app/
```

Add:

```
POSTGRES_DB=alxtravel
POSTGRES_USER=alxuser
POSTGRES_PASSWORD=alxpass
POSTGRES_HOST=localhost
POSTGRES_PORT=5433
```

---

# 🧱 **Running Migrations**

Use the inner manage.py:

```bash
cd alx_travel_app_0x00/alx_travel_app
python manage.py makemigrations
python manage.py migrate
```

---

# 🧩 **Models Implemented**

Inside `listings/models.py`:

* `Listing`: represents properties that users can book
* `Booking`: represents reservations linked to a listing
* `Review`: represents guest reviews for a listing

Each model includes:

* Fields
* Relationships (`ForeignKey`)
* Constraints
* Auto-generated timestamps

---

# 🧬 **Serializers Implemented**

Located in `listings/serializers.py`:

* `ListingSerializer`
* `BookingSerializer`
* `ReviewSerializer`

These convert model instances ↔ JSON.

---

# 🌱 **Database Seeding Command**

A custom management command was created at:

```
listings/management/commands/seed.py
```

Run the seeder:

```bash
python manage.py seed
```

This inserts several sample `Listing` objects into the database.

---

# 🧪 **Testing Seeder & Database**

Connect to the Postgres DB:

```bash
docker exec -it alxtravel_postgres bash
psql -U alxuser -d alxtravel
```

View tables:

```sql
\dt
SELECT * FROM listings_listing;
```

Exit:

```sql
\q
exit
```

---

# 📌 **Common Commands Summary**

### Start server

```bash
python manage.py runserver
```

### Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Seed the database

```bash
python manage.py seed
```

### Access Postgres shell

```bash
docker exec -it alxtravel_postgres bash
psql -U alxuser -d alxtravel
```

---

# ✔️ Milestone Complete

This project now includes:

* Fully structured Django models
* DRF serializers
* Seeding command
* PostgreSQL integration

