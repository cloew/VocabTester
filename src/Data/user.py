from kao_flask.ext.sqlalchemy.database import db

import random
from hashlib import sha1

class User(db.Model):
    """ Represents a user """
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text(), nullable=False, unique=True)
    password = db.Column(db.UnicodeText(), nullable=False)
    givenName = db.Column(db.UnicodeText())
    lastName = db.Column(db.UnicodeText())
    
    def __init__(self, **kwargs):
        """ Initialize the User """
        if kwargs['password']:
            kwargs['password'] = make_password(kwargs['password'])
        db.Model.__init__(self, **kwargs)
        
    def checkPassword(self, rawPassword):
        """ Check if the password is this users password """
        return check_password(rawPassword, self.password)
    
# borrowing these methods, slightly modified, from flask-peewee which in turn borrowed from django.contrib.auth
def get_hexdigest(salt, raw_password):
    data = salt + raw_password
    return sha1(data.encode('utf8')).hexdigest()

def make_password(raw_password):
    salt = get_hexdigest(unicode(random.random()), unicode(random.random()))[:5]
    hsh = get_hexdigest(salt, raw_password)
    return '%s$%s' % (salt, hsh)

def check_password(raw_password, enc_password):
    salt, hsh = enc_password.split('$', 1)
    return hsh == get_hexdigest(salt, raw_password)