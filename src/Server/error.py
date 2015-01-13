
class Error:
    """ Represents a Server Error """
    
    def __init__(self, code, message):
        """ Initialize the Error with its code and message """
        self.code = code
        self.message = message
        
    def toJSON(self):
        """ Transform the error into JSON """
        return {'code':self.code, 'message':self.message}
        
INVALID_CREDS = Error(1, 'Invalid Credentials')