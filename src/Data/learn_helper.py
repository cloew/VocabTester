from .Mastery import Mastery, StalenessPeriod

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
            learnedCache.add(form.id)
        
    def learn(self, form):
        """ Create the connection between the user and the form """
        self.field.append(form)
        self.user.save()
        
    def formsFor(self, language):
        """ Return the learned forms for the given language """
        formModel = self.formInfo.formModel
        return self.field.filter_by(language_id=language.id)\
                         .outerjoin(Mastery, (Mastery.user_id==self.user.id) & (getattr(Mastery, self.formInfo.masteryFieldName) == formModel.id))\
                         .outerjoin(StalenessPeriod)\
                         .order_by(formModel.ratingFor(self.user))\
                         .all()
        
    @property
    def field(self):
        """ Return the proper field """
        return getattr(self.user, self.formInfo.learnedField)