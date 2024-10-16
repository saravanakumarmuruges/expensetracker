# Django App

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#run-the-application-locally)
- [Docker Deployment](#docker-deployment)
- [Environment Variables](#environment-variables)

## Introduction
This Django-based web application is designed to update personal cash flow and keep track of all transactions like income, expenses and savings.

## Features
- User authentication and authorization.
- CRUD operations to create, update and delete tables transactions, income_type, expense_type, savings_type and users. 
- With this base APIs, it can be extended to any further user-friendly applications.

## Technologies Used
- **Django** - The web framework used for developing the app
- **PostgreSQL/MySQL/SQLite** - Database
- **Docker** (optional) - Containerization
- **AWS** (optional) - Cloud hosting and deployment
- **HTML/CSS/JavaScript** - Frontend

## Setup Instructions

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- Django 4.x
- Virtualenv (optional but recommended)
- Docker (if using Docker for deployment)

### Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
### Create and activate a virtual environment
```bash
python -m venv env
source env/bin/activate  # For Windows, use `env\Scripts\activate`
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Migrate the database
```bash
python manage.py migrate
```

### Create a superuser
```bash
python manage.py createsuperuser
```

### Run the application locally
```bash
python manage.py runserver
```

## Docker Deployment

### Build the Docker image
```bash
docker buildx build -t your-tag-name .
```

### Run the container
```bash
docker run -d -p 8000:8000 your-app-name
```

## Environment Variables
The following environment variables should be configured for proper functioning of the app:
```bash
SECRET_KEY: Django secret key for security
DEBUG: Set to False in production
DATABASE_URL: Connection URL for the database
ALLOWED_HOSTS: Comma-separated list of allowed hosts
```
