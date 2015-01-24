
class LearnedTracker:
    """ Helper Class for tracking learned aspects """
    
    def __init__(self, parent, fieldName, modelClass):
        """ Initialize the Tracker with the parent and its field to track with """
        self.parent = parent
        self.fieldName = fieldName
        self.modelClass = modelClass
        
    def learn(self, aspect):
        """ Create the connection between the parent and the aspect """
        getattr(self.parent, self.fieldName).append(aspect)
        self.parent.save()
        
    def hasLearned(self, id):
        """ Return if the parent has learned the aspect related to this id """
        return self.modelClass.query.filter_by(id=self.parent.id).filter(self.column.any(id=id)).first() != None
        
    @property
    def column(self):
        """ Return the proper column """
        return getattr(self.modelClass, self.fieldName)
        