from .concept_manager import ConceptManager
import functools

class ConceptPairRetriever(object):
    """ Helper descriptor to provide method to retrieve concept pairs """
    
    def __init__(self, formClass):
        """ Initialize the Concept Pair Retriever with the form class to use """
        self.conceptManager = ConceptManager(formClass)
        
    def __get__(self, obj, objtype=None):
        """ Return this descriptor or the getConceptPairs method """
        if obj is None:
            return self
        return functools.partial(self.getConceptPairs, obj)
    
    def getConceptPairs(self, parent, nativeLanguage, foreignLanguage):
        """ Return the concept pairs """
        conceptIds = [concept.id for concept in parent.concepts]
        return self.conceptManager.getConceptPairs(conceptIds, nativeLanguage, foreignLanguage)