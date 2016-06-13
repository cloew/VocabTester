from .concept import Concept
from .concept_pair import ConceptPair
            
class ConceptManager:
    """ Helper class to get the proper forms from Concepts """
    
    def __init__(self, conceptFormCache, languages):
        """ Initialize the Concept Manager with the Concept Form Cache and the Language Context """
        self.conceptFormCache = conceptFormCache
        self.languages = languages
        
    def findConceptMatchesAsList(self, conceptIds, language):
        """ Return the words matching the given concepts """
        return self.conceptFormCache.getAll(conceptIds=conceptIds, languageId=language.id)
        
    def findConceptMatchesAsDictionary(self, conceptIds, language):
        """ Return the words matching the given concepts """
        return self.conceptFormCache.getConceptDict(conceptIds=conceptIds, languageId=language.id)
    
    def getConceptIdsToNativeForms(self, conceptIds):
        """ Return the native forms for the list """
        return self.findConceptMatchesAsDictionary(conceptIds, self.languages.native)
		
    def getConceptIdsToForeignForms(self, conceptIds):
        """ Return the foreign forms in the list """
        return self.findConceptMatchesAsDictionary(conceptIds, self.languages.foreign)
    
    def getNativeForms(self, conceptIds):
        """ Return the native forms for the list """
        return self.findConceptMatchesAsList(conceptIds, self.languages.native)
		
    def getForeignForms(self, conceptIds):
        """ Return the foreign forms in the list """
        return self.findConceptMatchesAsList(conceptIds, self.languages.foreign)
    
    def getConceptPairs(self, conceptIds):
        """ Return the concept pairs """
        nativeForms = self.getConceptIdsToNativeForms(conceptIds)
        foreignForms = self.getConceptIdsToForeignForms(conceptIds)
        
        pairs = []
        for conceptId in conceptIds:
            if conceptId in nativeForms and conceptId in foreignForms:
                pairs.append(ConceptPair(nativeForms[conceptId], foreignForms[conceptId]))
        return pairs