from kao_flask.ext.sqlalchemy.database import db

from concept_list import ConceptList
from concept_pair import ConceptPair
from language import Language
from query_proxy import QueryProxy

class WordList:
    """ Represents a list of words to quiz """
    
    def __init__(self, conceptList):
        """ Initialize the Word List """
        self.conceptList = conceptList
        
    @property
    def concepts(self):
        return self.conceptList.concepts
        
    @property
    def id(self):
        return self.conceptList.id
        
    @property
    def name(self):
        return self.conceptList.name
    
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
        
WordList.query = QueryProxy(WordList, model=ConceptList)