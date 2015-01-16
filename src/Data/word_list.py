from kao_flask.ext.sqlalchemy.database import db

from concept_list import ConceptList
from language import Language
from concept_pair import ConceptPair

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
        
class QueryProxy:
    def __init__(self, queryModel, clsToReturn):
        """ Initialize the Query Proxy """
        self.queryModel = queryModel
        self.clsToReturn = clsToReturn
        self.__query = None
        
    def __getattr__(self, name):
        if hasattr(self, name):
            return getattr(self, name)
        elif self.query:
              return getattr(self.query, name )
        else:
              raise Exception( 'attribute %s not found' % name )
        
    @property
    def query(self):
        """ Return the user's native language """
        if self.__query is None:
            self.__query = self.queryModel.query
        return self.__query
              
    def first(self):
        """ Return the first query result """
        return self.clsToReturn(self.query.first())
        
    def all(self):
        """ Return all the query results """
        return [self.clsToReturn(entry) for entry in self.query.all()]
        
WordList.query = QueryProxy(ConceptList, WordList)