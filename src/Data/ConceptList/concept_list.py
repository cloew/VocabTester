from ..Concept import Concept
from ..query_proxy import query_via
from kao_decorators import proxy_for

from kao_flask.ext.sqlalchemy import db

concept_list_concepts = db.Table('concept_list_concepts', db.Model.metadata,
                                  db.Column('concept_list_id', db.Integer, db.ForeignKey('concept_lists.id', ondelete="CASCADE")),
                                  db.Column('concept_id', db.Integer, db.ForeignKey('concepts.id', ondelete="CASCADE")))

class ConceptList(db.Model):
    """ Represents a list of concepts """
    __tablename__ = 'concept_lists'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode())
    isWords = db.Column(db.Boolean)
    concepts = db.relationship("Concept", secondary=concept_list_concepts)
    
    def getConceptPairs(self, conceptManager):
        """ Return the concept pairs """
        return conceptManager.getConceptPairs([concept.id for concept in self.concepts])
    
def query_via_concept_list(isWords=None):
    def addQuery(cls):
        return query_via(lambda: ConceptList.query.filter_by(isWords=isWords))(cls)
    return addQuery

def concept_list_proxy(fieldName):
    return proxy_for(fieldName, ["id", "name", "concepts", "getConceptPairs"])