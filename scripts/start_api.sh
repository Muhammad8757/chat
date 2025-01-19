#!/bin/ash
echo "DJANGO_ENV is ${DJANGO_ENV}"
python3 manage.py runserver 0.0.0.0:8000
