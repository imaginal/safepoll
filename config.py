# -*- coding: utf-8 -*-

ADMINS = ['flyonts@gmail.com']
BRANDING = 'safepoll.me'
DEBUG = True
DATABASE = {
    'name': 'peewee.db',
    'engine': 'peewee.SqliteDatabase',
    'check_same_thread': False
}
SECRET_KEY = 'M2gcpjcHibNCkuegqDQr'

# Gunicorn
bind = '127.0.0.1:4000'
daemon = True
debug = DEBUG
workers = 1 if debug else 3
max_requests = 500
pidfile = 'gunicorn.pid'
accesslog = 'access.log'
errorlog = 'errors.log'
