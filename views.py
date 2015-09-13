# -*- coding: utf-8 -*-


from flask import *
from flask_peewee.utils import get_object_or_404

from app import app
from models import *
from ticket import VotingTicket, VotingBallot

@app.route('/favicon.ico')
def favicon():
    return ""


@app.route('/')
def main(template_name="main.html"):
    return render_template(template_name)


@app.route('/auth/')
def auth(template_name="auth.html"):
    ticket = VotingTicket()
    ticket.open_key('../keys/key1.pem')
    ticket.new_salt()
    ticket.set_data(1)
    ticket.sign()
    text = ticket.to_text()
    return render_template(template_name, ticket=text)


@app.route('/vote/', methods=['GET', 'POST'])
def vote(template_name="vote.html"):
    return render_template(template_name)

