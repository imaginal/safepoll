# -*- coding: utf-8 -*-

ADMINS = ['flyonts@gmail.com']
BRANDING = 'E-Voting'
DEBUG = False
DATABASE = {
    'name': 'peewee.db',
    'engine': 'peewee.SqliteDatabase',
    'check_same_thread': False
}
UPLOAD_DIR = '../var/uploads'
BALLOT_DIR = '../var/ballots'
SECRET_KEY = 'changeme-secret'
# OpenSSL
UADSTU_OPENSSL = '/usr/bin/openssl'
UADSTU_CER_DIR = '../var/certificates'

# Gunicorn
bind = '127.0.0.1:4000'
daemon = True
debug = DEBUG
workers = 1 if debug else 3
max_requests = 500
pidfile = 'gunicorn.pid'
accesslog = 'access.log'
errorlog = 'errors.log'
