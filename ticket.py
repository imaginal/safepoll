# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from base64 import b64encode, b64decode
from os import urandom

class SignedTicket:
    def open_key(self, fn):
        with open(fn) as f:
            self.key = RSA.importKey(f.read())
            self.signer = PKCS1_v1_5.new(self.key)

    def new_salt(self):
        self.salt = b64encode(urandom(21))

    def get_data(self):
        return self.data+'$'+self.salt

    def set_data(self, data):
        self.data = str(data)

    def sign(self):
        dgst = SHA256.new(self.get_data())
        self.signature = self.signer.sign(dgst)
        return self.signature

    def verify(self):
        dgst = SHA256.new(self.get_data())
        return self.signer.verify(dgst, self.signature)

    def split_by(self, seq, n):
        while seq:
            yield seq[:n]
            seq = seq[n:]

    def get_begin(self):
        return "---------- BEGIN %s ----------\n" % self.name

    def get_end(self):
        return "----------- END %s -----------\n" % self.name

    def get_b64signature(self):
        return b64encode(self.signature)

    def to_text(self):
        data = self.get_b64signature() + "$" + self.get_data()
        text = self.get_begin()
        text += "\n".join(self.split_by(data, 42)) + "\n"
        text += self.get_end()
        return text

    def from_text(self, text):
        begin = self.get_begin()
        pos = text.find(begin) + len(begin)
        text = text[pos:]
        pos = text.find(self.get_end())
        text = text[:pos].replace("\n", "").replace("\r", "")
        args = text.split("$")
        self.data = args[0]
        self.salt = args[1]
        self.signature = b64decode(args[2])


class VotingTicket(SignedTicket):
    name = 'VOTING TICKET'

class VotingBallot(SignedTicket):
    name = 'VOTING BALLOT'

