#!/usr/bin/env sh
python manage.py migrate
uwsgi --ini setup.cfg
