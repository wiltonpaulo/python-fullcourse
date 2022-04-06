# Setup python3

```console
 $ cd project-api
 $ python3 -m venv .venv
 $ source .venv/bin/activate
 $ pip3 install flask
 $ pip3 install flask-sqlalchemy
 $ pip3 freeze > requirements.txt
```

# Create table

```console
$ python
>>> from application import db
>>> db.create_all()
```

# Start application

```console
$ export FLASK_APP=application.py
$ flask run
```

# Using curl to access the api (http://localhost:5000)

```console
$ URL=http://localhost:5000

# Add new drinks (POST)
$ curl -X POST $URL/drinks \
   -H 'Content-Type: application/json' \
   -d '{"name":"Water","description":"vital for everyone"}'
$ curl -X POST $URL/drinks \
   -H 'Content-Type: application/json' \
   -d '{"name":"Coffee","description":"it keeps you awake"}'
$ curl -X POST $URL/drinks \
   -H 'Content-Type: application/json' \
   -d '{"name":"Juice","description":"liquid fruit"}'

# Retrieve all drinks informations (GET)
$ curl -X POST $URL/drinks
$ curl -X POST $URL/drinks/1

# Delete drink
$ curl -X DELETE $URL/drinks/1 \
    -H 'Content-Type: application/json'

# TODO Update drink data
$ curl -X PUT $URL/drinks \
   -H 'Content-Type: application/json' \
   -d '{"name":"Water","description":"vital for everyone"}'

```
