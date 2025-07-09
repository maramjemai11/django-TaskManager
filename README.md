# # 🗂️ Django Task Manager with REST API
readme changed on branch1
A personal task management web application built with Django and Django REST Framework. Users can register, log in, and manage their own tasks via a web interface or API. The project was created as part of my internship to learn development using Django.

---

## 🚀 Features

* User registration and login (web and API)
* JWT-based authentication (secure API access)
* Task CRUD (create, read, update, delete)
* Task fields: title, description, due date, status, priority
* Filter and sort tasks by status or fields
* Dashboard showing task stats (pending, in-progress, completed)
* Responsive UI with Bootstrap 5
* REST API with endpoints for external clients or mobile apps

---

## 🛠️ Tech Stack

* **Backend:** Django 5.x, Django REST Framework, Simple JWT
* **Frontend:** Django Templates, Bootstrap 5, HTML5, CSS3
* **Database:** SQLite (default)
* **Tools:** Insomnia / Postman for API testing

---

## 📁 Project Structure

```
django-task-manager/
├── manage.py
├── myproject/           # Project settings and root URLs
├── tasks/               # Main app: models, views, serializers, forms, URLs
├── templates/           # HTML templates
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── ...
```

---

## 📦 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/maramjemai11/django-task-manager.git
cd django-task-manager
```

2. **Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory:

```bash
touch .env
```

Inside `.env`, add:

```env
SECRET_KEY='your-django-secret-key'
DEBUG=True
```

5. **Run database migrations**

```bash
python manage.py migrate
```

6. **Start the development server**

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📚 Dependencies

Key dependencies (see `requirements.txt` for full list):
- Django >=5.0
- djangorestframework
- djangorestframework-simplejwt
- python-dotenv
- (and others)

To add a new dependency:
```bash
pip install <package>
pip freeze > requirements.txt
```

---

## 🔐 API Authentication (JWT)

* `POST /api/token/` — Obtain token
* `POST /api/token/refresh/` — Refresh token
* Use the token in request headers:

  ```
  Authorization: Bearer <your_token>
  ```

---

## 📚 API Endpoints

* `GET /api/tasks/` — List tasks
* `POST /api/tasks/` — Create a task
* `PUT /api/tasks/<id>/` — Update a task
* `DELETE /api/tasks/<id>/` — Delete a task
* `POST /api/register/` — Register a new user

---

## 🙋‍♀️ Author

**Maram Jemai**
GitHub: [maramjemai11](https://github.com/maramjemai11)

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
