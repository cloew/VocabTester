from .concept import Concept
from .concept_pair import ConceptPair
from .word import Word
            
class ConceptManager:
    """ Helper class to get the proper forms from Concepts """
    
    def __init__(self, conceptFormCache, nativeLanguage, foreignLanguage):
        """ Initialize the Concept Manager """
        self.conceptFormCache = conceptFormCache
        self.nativeLanguage = nativeLanguage
        self.foreignLanguage = foreignLanguage
    
    def findConceptMatches(self, conceptIds, language):
        """ Return the words matching the given concepts """
        return self.conceptFormCache.getAll(conceptIds=conceptIds, languageId=language.id)
    
    def getNativeForms(self, conceptIds):
        """ Return the native forms for the list """
        return self.findConceptMatches(conceptIds, self.nativeLanguage)
		
    def getForeignForms(self, conceptIds):
        """ Return the foreign forms in the list """
        return self.findConceptMatches(conceptIds, self.foreignLanguage)
    
    def getConceptPairs(self, conceptIds):
        """ Return the concept pairs """
        nativeForms = self.getNativeForms(conceptIds)
        foreignForms = self.getForeignForms(conceptIds)
        return [ConceptPair(native, foreign) for native, foreign in zip(nativeForms, foreignForms)]