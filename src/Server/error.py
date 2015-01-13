
class Error:
    """ Represents a Server Error """
    
    def __init__(self, code, message):
        """ Initialize the Error with its code and message """
        self.code = code
        self.message = message
        
    def toJSON(self):
        """ Transform the error into JSON """
        return {'error':{'code':self.code, 'message':self.message}}
        
INVALID_CREDS = Error(1, 'Invalid Credentials')
EMAIL_IN_USE = Error(2, 'The provided email address is already in use')