from .concept import Concept
from .concept_pair import ConceptPair
            
class ConceptManager:
    """ Helper class to get the proper forms from Concepts """
    
    def __init__(self, conceptFormCache, languages):
        """ Initialize the Concept Manager with the Concept Form Cache and the Language Context """
        self.conceptFormCache = conceptFormCache
        self.languages = languages
        
    def findConceptMatches(self, conceptIds, language):
        """ Return the words matching the given concepts """
        return self.conceptFormCache.getAll(conceptIds=conceptIds, languageId=language.id)
    
    def getNativeForms(self, conceptIds):
        """ Return the native forms for the list """
        return self.findConceptMatches(conceptIds, self.languages.native)
		
    def getForeignForms(self, conceptIds):
        """ Return the foreign forms in the list """
        return self.findConceptMatches(conceptIds, self.languages.foreign)
    
    def getConceptPairs(self, conceptIds):
        """ Return the concept pairs """
        nativeForms = self.getNativeForms(conceptIds)
        foreignForms = self.getForeignForms(conceptIds)
        return [ConceptPair(native, foreign) for native, foreign in zip(nativeForms, foreignForms)]