from concept import Concept
from concept_pair import ConceptPair
from word import Word
            
class ConceptManager:
    """ Helper class to get the proper forms from Concepts """
    
    def __init__(self, conceptFormClass):
        """ Initialize the Concept Manager """
        self.conceptFormClass = conceptFormClass
    
    def findConceptMatches(self, conceptIds, language):
        """ Return the words matching the given concepts """
        return self.conceptFormClass.query.filter(self.conceptFormClass.concept_id.in_(conceptIds), self.conceptFormClass.language_id==language.id).order_by(self.conceptFormClass.concept_id).all()
    
    def getNativeForms(self, conceptIds, user):
        """ Return the native forms for the list """
        return self.findConceptMatches(conceptIds, user.nativeLanguage)
		
    def getForeignForms(self, conceptIds, user):
        """ Return the foreign forms in the list """
        return self.findConceptMatches(conceptIds, user.foreignLanguage)
    
    def getConceptPairs(self, conceptIds, user):
        """ Return the concept pairs """
        nativeForms = self.getNativeForms(conceptIds, user)
        foreignForms = self.getForeignForms(conceptIds, user)
        return [ConceptPair(native, foreign) for native, foreign in zip(nativeForms, foreignForms)]