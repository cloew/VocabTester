from .concept import Concept
from .concept_pair import ConceptPair
from .word import Word
            
class ConceptManager:
    """ Helper class to get the proper forms from Concepts """
    
    def __init__(self, conceptFormCache):
        """ Initialize the Concept Manager """
        self.conceptFormCache = conceptFormCache
    
    def findConceptMatches(self, conceptIds, language):
        """ Return the words matching the given concepts """
        return self.conceptFormCache.getAll(conceptIds=conceptIds, languageId=language.id)
    
    def getNativeForms(self, conceptIds, nativeLanguage):
        """ Return the native forms for the list """
        return self.findConceptMatches(conceptIds, nativeLanguage)
		
    def getForeignForms(self, conceptIds, foreignLanguage):
        """ Return the foreign forms in the list """
        return self.findConceptMatches(conceptIds, foreignLanguage)
    
    def getConceptPairs(self, conceptIds, nativeLanguage, foreignLanguage):
        """ Return the concept pairs """
        nativeForms = self.getNativeForms(conceptIds, nativeLanguage)
        foreignForms = self.getForeignForms(conceptIds, foreignLanguage)
        return [ConceptPair(native, foreign) for native, foreign in zip(nativeForms, foreignForms)]