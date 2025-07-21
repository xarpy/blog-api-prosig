# Blog API Challenge

RESTful API for a simple blogging platform using Django and Django REST Framework.

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.16-orange.svg)](https://www.django-rest-framework.org/)

---

## 📚 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Installation

Clone the project and install dependencies:

```bash
git@github.com:xarpy/blog-api-prosig.git
cd blog-api-prosig
pip install -r requirements/dev.txt
```

**Obs:**
You can create your super user, using the command: `python manage.py createsuperuser`, if won't, just use my test such as exmaple for that, *username*: **test_only**, *password*: **12345**.
Dont forget to convert the file env.example to .env file

Apply migrations and load test data:

```bash
python manage.py migrate
python manage.py loaddata fixtures/adminuser.json
python manage.py loaddata fixtures/test_data.json
```

Run server:

```bash
python manage.py runserver
```

---

## 🧪 Testing

Run all tests with:

```bash
pytest
```

If using Docker:

```bash
docker compose exec backend pytest
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /api/v1/posts/ | List all blog posts |
| POST   | /api/v1/posts/ | Create a new blog post |
| GET    | /api/v1/posts/{uuid}/ | Get a single blog post with comments |
| POST   | /api/v1/posts/{uuid}/comments/ | Add a comment to a post |
| POST   | /api/v1/token/ | Get JWT access & refresh tokens |
| POST   | /api/v1/token/refresh/ | Refresh the JWT token |

---

## 📄 Documentation
<img width="1513" height="1279" alt="2025-07-21_02-54" src="https://github.com/user-attachments/assets/8fcae136-740c-45fe-bb06-4e2a07a07aee" />
<img width="1536" height="1389" alt="2025-07-21_04-12" src="https://github.com/user-attachments/assets/1333cbda-6177-4eb9-8307-f831747ff2c6" />


Swagger UI available at:

Inside docker:
```
http://localhost/api/docs/
```

Local Environment:
```
http://localhost:8000/api/docs/
```
---

## 🤝 Contributing

Feel free to submit issues or pull requests. To contribute:

```bash
git checkout -b feature/your-feature
git commit -m "feat: add your feature"
git push origin feature/your-feature
```

Then open a Pull Request.

---

## 🪪 License

This project is licensed under the MIT License.
