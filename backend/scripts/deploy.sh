#!bin/sh

python manage.py collectstatic --no-input
python check_db.py
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py initadmin
python manage.py runserver 0:8000

NAME="app"
DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
USER=app
GROUP=app
NUM_WORKERS=5
DJANGO_WSGI_MODULE=config.wsgi

gunicorn ${DJANGO_WSGI_MODULE}:application \
   --bind 0.0.0.0:8000 \
   --name $NAME \
   --worker-connections 1000 \
   --workers $NUM_WORKERS \
   --user $USER \
   --group $GROUP