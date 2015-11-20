import random
from hashlib import sha1

def get_hexdigest(salt, raw_password):
    data = salt + raw_password
    return sha1(data.encode('utf8')).hexdigest()
    
class LegacyPasswordUtil:
    """ Helper class to make and check passwords """
    
    # borrowing these methods, slightly modified, from flask-peewee which in turn borrowed from django.contrib.auth
    def make(self, raw_password):
        """ Return the hashed password """
        salt = get_hexdigest(str(random.random()), str(random.random()))[:5]
        hsh = get_hexdigest(salt, raw_password)
        return '%s$%s' % (salt, hsh)
        
    def check(self, raw_password, enc_password):
        """ Return if the Passowrd provided is valid """
        salt, hsh = enc_password.split('$', 1)
        return hsh == get_hexdigest(salt, raw_password)