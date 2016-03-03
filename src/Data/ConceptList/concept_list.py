from ..Concept import Concept
from ..filtered_query import FilteredQuery
from ..Mastery import Mastery, StalenessPeriod

from kao_flask.ext.sqlalchemy import db
from sqlalchemy import func
from sqlalchemy.ext.hybrid import hybrid_method

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
    
    @hybrid_method
    def averageRatingFor(self, language, conceptFormCache, masteryCache):
        """ Return the rating for the given user """
        ratings = []
        for concept in self.concepts:
            form = conceptFormCache.get(conceptId=concept.id, languageId=language.id)
            ratings.append(masteryCache[form.id].rating)
        return round(sum(ratings, 0.0) / len(ratings), 1)
    
    @averageRatingFor.expression
    def averageRatingFor(self, user, language):
        """ Return the rating for the given user """
        return func.avg(self.entry_model.ratingFor(user)).over(partition_by=self.id)
    
def bound_concept_list(*, isWords):
    def bind(cls):
        def init(self, *args, **kwargs):
            kwargs['isWords'] = isWords
            ConceptList.__init__(self, *args, **kwargs)
        cls.__init__ = init
        cls.query = FilteredQuery(ConceptList, isWords=isWords)
        return cls
    return bind