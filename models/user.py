import datetime as dt

from marshmallow import Schema, fields, INCLUDE

class User(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.createdAt=dt.datetime.now()
    
    def __repr__(self):
        return '<User(name={self.email!r})>'.format(self=self)


class UserSchema(Schema):
    id = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    class Meta:
        unknown = INCLUDE
    