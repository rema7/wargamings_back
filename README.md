# Wargaming

## Install

##### Prepare environment

```python
pip3 install virtualenv
virtualenv env
source env/bin/activate
```
#####  Install Django 1.9 or 1.10

version 1.9
```apple js
pip install Django==1.9.6 
```
version 1.10
```apple js
pip install django
```
####Install libraries dependency

```
pip install djangorestframework django-cors-headers names
```

##### Initiate Django

```
./manage.py migrate
```

## Generate players

```
./manage.py gen_players
```

You can use optional parameter ``--number 10`` to set number generated players

Example usage: ``./manage.py gen_players --number 20``

## Admin

Create admin user
```
./manage.py createsuperuser
```

You can see information about user here
``http://127.0.0.1:8000/admin/players/player/``


## Run server
```
./manage.py runserver
```

Server address ``http://127.0.0.1:8000/`` 

