# Titanic

In this project I create an web app to know if you had been survived in the Titanic thank to a Machine Learning model that I created.

## How to know if I had survived in Titanic?
Send the following structure in your request an a Machine Learning model will response you.
```
POST http://127.0.0.1:8000/api/v1/passenger/predict/
Content-Type: application/json

{
    "Class": "1",
    "Name": "John Doe",
    "Gender": "male",
    "Age": 12,
    "SibSp": 0,
    "ParCh": 0,
    "Fare": 2.50,
    "Embarked": "Southampton"
}
```
Here:
- `SibSp` is the quantity of your siblings and spouses on board.
- `ParCh` is the quantity of your parents and children on board.
- `Fare` is how much would you have paid to get your ticket. 
- `Embarked` is where you embarked. 

You can see the rest endpoints in `backend/api.http`.

## What I used
- Django
- Django Rest Framework
- Postgres
- Scikit Learn
- Pandas
- NumPy
- matplotlib
- Docker
- Docker Compose

## How to run it?
Set the environmental variables in `backend/.env.exanple` and change the name of the file to `.env`.

### Development
#### Local
Install the requirements:
```
pip install -r requirements.dev.txt
```
Execute the following commands to run it locally:
```
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py initadmin
python manage.py populate_db
python manage.py runserver 0:8000
```
#### Docker
Execute the following commands to run with Docker
##### Backend
Build Docker image in `backend/` directory
```
docker build -f Dockerfile.dev --rm -t back .
```
Creating container to develop in `/`
```
docker run \
   --rm \
   --hostname back \
   --name back \
   -v $PWD/backend:/home/app \
   -p 8000:8000 \
   -it \
   back
```

#### Docker Compose
Execute the following code to run:
```
docker compose \
   --env-file=backend/.env \
   -f docker-compose.dev.yml \
   up
```
And the next one to stop:
```
docker compose -f docker-compose.dev.yml down
```

### Production
#### Local
Set the system environmental variable `PROD` to `ON`

Install the requirements:
```
pip install -r requirements.prod.txt
```
Execute the following commands to run it locally:
```
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py initadmin
python manage.py populate_db
python manage.py runserver 0:8000
```
#### Docker
Execute the following commands to run with Docker
##### Creating network
```
docker network create back-db
```
##### Database
Creating Postgres container
```
docker run \
   --rm \
   --network back-db \
   --hostname db \
   --name db \
   -e POSTGRES_USER=pguser \
   -e POSTGRES_PASSWORD=asd123 \
   -e POSTGRES_DB=app \
   -v $PWD/database:/var/lib/postgresql/data \
   -p 5432:5432 \
   postgres:16.0-alpine
```
**NOTE**: Set the same environmentals in `backend/.env`

Connect to database
```
docker exec -it db psql -U pguser -d app
```
##### Backend
Build Docker image in `backend/` directory
```
docker build -f Dockerfile.prod --rm -t back .
```
Creating container to develop in `/`
```
docker run \
   --rm \
   --network back-db \
   --hostname back \
   --name back \
   -e PROD=ON \
   -v $PWD/backend:/home/app \
   -p 8000:8000 \
   -it \
   back
```

#### Docker Compose
Execute the following code to run:
```
docker compose \
   --env-file=backend/.env \
   -f docker-compose.prod.yml \
   up
```
And the next one to stop:
```
docker compose -f docker-compose.prod.yml down
```

## Where is this running?
It is running on:
```
http://127.0.0.1:8000
```
in all cases