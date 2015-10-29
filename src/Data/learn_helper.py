
class LearnHelper:
    """ Helper Class for learning forms """
    
    def __init__(self, user, formInfo):
        """ Initialize the Helper with the User and Form Info """
        self.user = user
        self.formInfo = formInfo
        
    def tryToLearn(self, form, learnedCache):
        """ Learn the form unless it is already learned """
        if form.id not in learnedCache:
            self.learn(form)
        
    def learn(self, form):
        """ Create the connection between the user and the form """
        getattr(self.user, self.fieldName).append(form)
        self.user.save()
        
    def formsFor(self, language):
        """ Return the learned forms for the given language """
        return self.column.filter_by(language_id=language.id).all()
        
    @property
    def column(self):
        """ Return the proper column """
        return getattr(self.user, self.formInfo.learnedField)
        