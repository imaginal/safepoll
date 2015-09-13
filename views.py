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
    if request.form:
        text = request.form['ticket']
        ticket = VotingTicket()
        ticket.open_key('../keys/key1.pem')
        ticket.from_text(text)
        if ticket.signature and ticket.data:
            return redirect('pick')
    return render_template(template_name)


@app.route('/pick/')
def pick(template_name="pick.html"):
    if request.args:
        pick_id = request.args['id']
        ballot = VotingBallot()
        ballot.open_key('../keys/key2.pem')
        ballot.new_salt()
        ballot.set_data(pick_id)
        ballot.sign()
        with open('static/results.txt', 'a') as f:
            s = ballot.get_b64signature()[0:80]
            r = "%s %s\n" % (pick_id, s)
            f.write(r)
        text = ballot.to_text()
        return render_template("done.html", ballot=text)

    return render_template(template_name)

