

# To-Do App (Django)

A simple and responsive **To-Do List web application** built with Django and Bootstrap.  
Users can **add, update, delete, and mark tasks as completed** on a single page.  

This version is **public**, so no login or authentication is required.

---

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as completed (tick)
- Responsive UI with **dark mode toggle**
- Fully public and mobile-friendly

---

## Technology Stack

- Backend: Django 5.2
- Frontend: Bootstrap 5
- Database: SQLite (default)
- Deployment: [Render](https://render.com)

---

## Deployment

The app is deployed and can be accessed at:

**[Live App Link](https://to-do-app-django-wx4x.onrender.com/)**

---

## Installation (Local Setup)

1. Clone the repository:

```bash
git clone https://github.com/Arman1263/To-Do-App-Django.git
cd To-Do-App-Django
````

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open your browser and go to:

```
http://127.0.0.1:8000/
```
