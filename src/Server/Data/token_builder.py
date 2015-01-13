import jwt

def BuildToken(user):
    """ Build the token """
    return jwt.encode({'email':user.email}, 'secret token')