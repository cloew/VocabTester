
class LearnedTracker:
    """ Helper Class for tracking learned aspects """
    
    def __init__(self, parent, fieldName, modelClass):
        """ Initialize the Tracker with the parent and its field to track with """
        self.parent = parent
        self.fieldName = fieldName
        self.modelClass = modelClass
        
    def tryToLearn(self, form):
        """ Learn the form unless it is already being tracked """
        if not self.hasLearned(form.id):
            self.learn(form)
        
    def learn(self, form):
        """ Create the connection between the parent and the form """
        getattr(self.parent, self.fieldName).append(form)
        self.parent.save()
        
    def hasLearned(self, id):
        """ Return if the parent has learned the form related to this id """
        return self.modelClass.query.filter_by(id=self.parent.id).filter(self.column.any(id=id)).first() != None
        
    @property
    def column(self):
        """ Return the proper column """
        return getattr(self.modelClass, self.fieldName)
        