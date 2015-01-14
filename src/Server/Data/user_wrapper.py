
class UserWrapper:
    """ Converts users to JSON """
    
    def __init__(self, user):
        """ Initialize the user wrapper """
        self.user = user
        
    def toJSON(self):
        """ Convert the word list to JSON """
        return {"id":self.user.id,
                "email":self.user.email,
                "givenName":unicode(self.user.givenName),
                "lastName":unicode(self.user.lastName)}