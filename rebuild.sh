#!/bin/bash

echo "Do you want to rebuild docker?: (y/n)"
read docker

if [ "$docker" == "y" ]; then
  docker-compose build
fi

echo "Do you want to run migration?: (y/n)"
read migration

if [ "$migration" == "y" ]; then
  docker-compose run web python manage.py migrate
  docker-compose run web python manage.py makemigrations
  docker-compose run web python manage.py migrate
fi

echo "Do you want to create a user?: (y/n)"
read user

if [ "$user" == "y" ]; then
  docker-compose run web python manage.py createsuperuser
fi