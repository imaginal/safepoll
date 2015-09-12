# -*- coding: utf-8 -*-

from flask_peewee.admin import Admin
from flask_peewee.auth import Auth

from app import app, db
from models import *

auth = Auth(app, db, user_model=User)
admin = Admin(app, auth, branding=app.config['BRANDING'])

auth.register_admin(admin)
#admin.register(Candidate)
admin.setup()
