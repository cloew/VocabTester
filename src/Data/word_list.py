from decorators import proxy_for

from concept_list import ConceptList
from concept_pair import ConceptPair
from language import Language
from query_proxy import query_via

from kao_flask.ext.sqlalchemy.database import db

@query_via(ConceptList)
@proxy_for('conceptList', ["id", "name", "concepts"])
class WordList:
    """ Represents a list of words to quiz """
    
    def __init__(self, conceptList):
        """ Initialize the Word List """
        self.conceptList = conceptList
    
    def getNativeWords(self, conceptManager, user):
        """ Return the native words in the word list """
        return conceptManager.findConceptMatches(self.concepts, user.nativeLanguage)
        
    def getForeignWords(self, conceptManager, user):
        """ Return the foreign words in the word list """
        return conceptManager.findConceptMatches(self.concepts, user.foreignLanguage)
        
    def getWordPairs(self, conceptManager, user):
        """ Return the word pairs """
        nativeForms = self.getNativeWords(conceptManager, user)
        foreignForms = self.getForeignWords(conceptManager, user)
        return [ConceptPair(native, foreign) for native, foreign in zip(nativeForms, foreignForms)]