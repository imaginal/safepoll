# -*- coding: utf-8 -*-

from datetime import datetime
from flask_peewee.auth import BaseUser
from peewee import *

from app import db


class User(db.Model, BaseUser):
    username = CharField(unique=True)
    password = CharField()
    join_date = DateTimeField(default=datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)
    email = property(lambda x: x.username)

    def __unicode__(self):
        return self.username


class Poll(db.Model):
    name = CharField()
    image = CharField()
    open_date = DateTimeField(default=datetime.now)
    close_date = DateTimeField(default=datetime.now)
    open_results = BooleanField(default=False)
    is_anonymous = BooleanField(default=True)
    is_public = BooleanField(default=True)
    audience = TextField(null=True)

    def __unicode__(self):
        return self.name


class Candidate(db.Model):
    poll = ForeignKeyField(Poll)
    name = CharField()
    slug = CharField(null=True, unique=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.upper().replace(' ', '_')
        return super(Candidate, self).save(*args, **kwargs)


class Ballot(db.Model):
    choice = ForeignKeyField(Candidate)
    salt = CharField()
    sign = CharField()

    def __unicode__(self):
        return self.salt


class Ticket(db.Model):
    poll = ForeignKeyField(Poll)
    salt = CharField()
    sign = CharField()

    def __unicode__(self):
        return self.salt


class UsedID(db.Model):
    poll = ForeignKeyField(Poll)
    code = CharField()

    def __unicode__(self):
        return self.code


def create_tables(create_admin_user=False):
    models = [User, Poll, Candidate, Ballot, Ticket, UsedID]
    for cls in models:
        cls.create_table()
    if create_admin_user:
        user = User(username='admin', admin=True)
        user.set_password('admin')
        user.save()
