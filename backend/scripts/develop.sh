#!bin/sh

python check_db.py
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py initadmin
python manage.py runserver 0:8000