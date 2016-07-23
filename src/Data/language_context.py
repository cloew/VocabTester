from kao_decorators import proxy_for

@proxy_for('languages', ['__iter__', '__contains__'])
class LanguageContext:
    """ Represents the Foreign and Native Language Context """
    
    def __init__(self, *, foreign, native):
        """ Initialize with the Foreign and Native Languages """
        self.foreign = foreign
        self.native = native
        self.languages = [foreign, native]
        
    def isForeign(self, form):
        """ Return whether the form is foreign """
        return form.language is self.foreign
        
    def isNative(self, form):
        """ Return whether the form is native """
        return form.language is self.native
        
    def __iter__(self):
        """ Return the iterator over the langauges """
        return iter([self.foreign, self.native])
        
    def __repr__(self):
        """ Return the String Representation of the Language Context """
        return repr(self.languages)