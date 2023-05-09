# django-acm-managment-system
![university of bozorgmehr](https://puya.buqaen.ac.ir/ui3/image/logo_v.png)

a system for manage acm challenge in the bozorgmehr university.

# Requirement
python3.11+

debian 11+ || ubuntu 22+

apache2 || ngnix

# Setup project
for setup project first create a venv for python envirement 
`python -m venv .venv`
after create .venv folder run this code for activate venv in terminal

`source .venv/bin/activate`

now need install the requirement package for runnnig the python-django script, install this packages with this command:

`pip install -r re.txt`

now we can run django project with `python manage.py runserver`. 🥳


# Deploy app
for deploing app on local system we need install `gunicorn` so can install this package with this command

`pip install gunicorn`

after installed package run this command for ready django database:

`python manage.py migrate`

then if you have other services of run on port 80, stop service. for example:

`sudo systemctl stop apache2`

after opened 80 port, run this command for runnig django script

`gunicorn settings.wsgi --bind 0.0.0.0:80`.

now for access to index page of site, run `ifconfig` command and find your ip address and open it in browser


# Access to admin pannel
open new terminal tab and activate .venv and in this path edit `NEED_ADMIN` to `True` same this

```python
# acm/settings/settings.py

...

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
NEED_ADMIN = False # --> Change this to True.

ALLOWED_HOSTS = [ ] # --> Add your ip address to this list.
AUTH_USER_MODEL = 'groups.Group'

...
```

after change it, run this command

`python manage.py runserver`

and after run open this link [click to open admin panel](http://localhost:8000/admin/)

> if does not exits Admin user in system create this command
> `python manage.py createsuperuser`
> fill the all questions and open again admin panel and login to Admin panel with selected username and password


