# adsPortal

A free platform for hosting ads of any kind. The Web application is written
in Django.

## Dependencies

- Python 3.10
- Docker & Docker Compose (optional)

## Development setup

### Clone this repository

```
$ git clone git@github.com:knaiskes/adsPortal.git
```

### Create a virtual enviroment and install project's dependencies

```
$ cd adsportal/
$ python -m venv venv
$ pip install -r requirements.txt
```

### Migrate and create super user

```
$ python manage.py migrate
$ python manage.py createsuperuser
```

Visit [localhost:8000/ads/](http://localhost:8000/ads/)


## Setup for development with Docker

### Fetch images and create containers

```
$ docker-compose up
```

### Migrate and create super user

```
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser
```

Visit [localhost:8000/ads/](http://localhost:8000/ads/)

### Remove Docker containers, volumes and network

```
$ docker-compose down -v
```

## Deploy infrastructure - Terraform

```
$ cd infrastructure/
$ terraform init
$ terraform apply
$ terraform show # get deployment information
```
