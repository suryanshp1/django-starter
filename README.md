# django-starter
A simple django starter page


## Commands to start django project

```bash
django-admin startproject a_core .
```

## Setup a database

```bash
python .\manage.py migrate
```

## Start server

```bash
python manage.py runserver
```

## Create a_home app

```bash
python manage.py startapp a_home
```

## Create a_users app

```bash
python manage.py startapp a_users
```

## make migrations for Profile model

```bash
python manage.py makemigrations  ## migration command to create migration file
python manage.py migrate  ## migrate to apply migration file
```

## create a super user

```bash
python manage.py createsuperuser  ## after that give username, email and password
```


## How to run ?


1. Create a virtual environment

```bash
python -m venv venv
```


2. Activate virtual environment

```bash
.\venv\Scripts\activate
```

3. install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Migrate to database

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. Run application

```bash
python manage.py runserver
```

6. Generate Secret Key

```bash
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```