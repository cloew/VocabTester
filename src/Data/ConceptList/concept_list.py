from ..Concept import Concept
from ..filtered_query import FilteredQuery

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
    
def bound_concept_list(*, isWords):
    def bind(cls):
        def init(self, *args, **kwargs):
            kwargs['isWords'] = isWords
            ConceptList.__init__(self, *args, **kwargs)
        cls.__init__ = init
        cls.query = FilteredQuery(ConceptList, isWords=isWords)
        return cls
    return bind