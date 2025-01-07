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

### Docker build and run commands

```bash
docker build -t my-docker-image . # build docker image
docker run -d -p 8001:8000 -v .:/app  my-docker-image  # run it on port 8001 and attach to volume to reflect the local code changes in container
```

### Docker compose command for developemnt environment

```bash
docker compose up -d --build # run containers through docker compose file
docker compose down --volumes # down the containers and removing volume
docker compose exec app python manage.py migrate --noinput # migration command
docker compose exec app python manage.py createsuperuser # create super user

## Common commands
docker system prune -a # delete all docker related data
docker exec -it <container-name/id> bash # open container in interactive mode
docker image ls or docker images # list all images
docker image rm <imagename/id> # remove image
docker image prune # remove images
docker container ls or docker ps # list containers
docker compose pull <container hostname>:<tagname> # to pull latest image
docker compose ps # list containers
docker stats # get resources use of containers
```

### Docker compose command for production environment

```bash
docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec app python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec app python manage.py collectstatic --no-input --clear
```