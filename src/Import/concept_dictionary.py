from Data.concept import Concept
from Server import server

class ConceptDictionary:
    """ Represents a dictionary of the concept Language Egg id to the Concept Data Model object """
    
    def __init__(self, eggs):
        """ Initialize the concept dictionary with the egg wrapper objects """
        self.idToConcept = {}
        for egg in eggs:
            for conceptId, form in egg.loadExisting():
                self.idToConcept[conceptId] = form.concept
                
    def __getitem__(self, conceptId):
        """ Return the concept for the given concept Id """
        if conceptId in self.idToConcept:
            return self.idToConcept[conceptId]
        else:
            concept = Concept()
            server.db.session.add(concept)
            self.idToConcept[conceptId] = concept
            return concept