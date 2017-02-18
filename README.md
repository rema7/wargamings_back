# Wargaming

## Install

Use next commands to install:

```python
pip3 install virtualenv
virtualenv env
source env/bin/activate
pip install django djangorestframework django-cors-headers names
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

