from decorators import proxy_for
from query_proxy import query_via
from concept import Concept
from concept_pair import ConceptPair

from kao_flask.ext.sqlalchemy.database import db

concept_list_concepts = db.Table('concept_list_concepts', db.Model.metadata,
                                  db.Column('concept_list_id', db.Integer, db.ForeignKey('concept_lists.id')),
                                  db.Column('concept_id', db.Integer, db.ForeignKey('concepts.id')))

class ConceptList(db.Model):
    """ Represents a list of concepts """
    __tablename__ = 'concept_lists'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode())
    isWords = db.Column(db.Boolean)
    concepts = db.relationship("Concept", secondary=concept_list_concepts)
    
def query_via_concept_list(isWords=None):
    def addQuery(cls):
        return query_via(lambda: ConceptList.query.filter_by(isWords=isWords))(cls)
    return addQuery

def concept_list_proxy(fieldName):
    return proxy_for(fieldName, ["id", "name", "concepts"])
    
def concept_pair_retriever(FormClass):
    def addMethods(cls):
        def findConceptMatches(self, language):
            """ Return the words matching the given concepts """
            conceptIds = [concept.id for concept in self.concepts]
            return FormClass.query.filter(FormClass.concept_id.in_(conceptIds), FormClass.language_id==language.id).order_by(FormClass.concept_id).all()
        
        def getNativeForms(self, user):
            """ Return the native forms for the list """
            return self.findConceptMatches(user.nativeLanguage)
            
        def getForeignForms(self, user):
            """ Return the foreign forms in the list """
            return self.findConceptMatches(user.foreignLanguage)
            
        def getConceptPairs(self, user):
            """ Return the concept pairs """
            nativeForms = self.getNativeForms(user)
            foreignForms = self.getForeignForms(user)
            return [ConceptPair(native, foreign) for native, foreign in zip(nativeForms, foreignForms)]
            
        cls.findConceptMatches = findConceptMatches
        cls.getNativeForms = getNativeForms
        cls.getForeignForms = getForeignForms
        cls.getConceptPairs = getConceptPairs
        return cls
    return addMethods