from kao_decorators import proxy_for

@proxy_for('conceptList', ['id', 'name'])
class BoundConceptList:
    """ Wrapper class to represent a ConceptList bound to the ConceptManager that provides the Forms for the appropriate LanguageContext """
    
    def __init__(self, conceptList, conceptManager):
        """ Initialize with the List and Concept Manager """
        self.conceptList = conceptList
        self.conceptManager = conceptManager
        
    @property
    def concepts(self):
        """ Return the concept pairs for the languages in the Concept Manager """
        return self.conceptList.getConceptPairs(self.conceptManager)
        
    def __repr__(self):
        """ Return the String Representation of the Bound Concept List """
        return "<BoundConceptList({0})>".format(self.conceptList)