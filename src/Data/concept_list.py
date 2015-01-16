from query_proxy import query_via
from concept import Concept

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