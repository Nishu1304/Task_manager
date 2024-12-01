# Task Manager with Google Authentication
## Overview
This is a Django-based Task Manager application that allows users to create, edit, and manage tasks. It also features user authentication, including Google sign-in via OAuth integration.

The application has the following key features:

User registration and login (including Google OAuth login).
Task creation, editing, and deletion.
Admin panel for managing users and tasks.

## Features
### User Authentication:
Register and log in using email/password.
Google OAuth integration for seamless sign-in.
### Task Management:
Create new tasks with a title and description.
Edit existing tasks.
Delete tasks.
### Admin Panel:
Manage users and their tasks.

## Prerequisites
Python 3.11+
Django 5.0.1
A Google Cloud Project with OAuth 2.0 credentials.


### Installation
Clone the repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


### Install dependencies:
pip install -r requirements.txt

### Apply migrations:
python manage.py migrate


### Create a superuser for admin access:
python manage.py createsuperuser


### Start the server:
python manage.py runserver

