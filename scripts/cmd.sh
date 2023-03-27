#!/usr/bin/env bash
python manage.py migrate
uwsgi --ini setup.cfg