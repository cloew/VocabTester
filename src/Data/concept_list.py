from kao_flask.ext.sqlalchemy.database import db

from concept import Concept

concept_list_concepts = db.Table('concept_list_concepts', db.Model.metadata,
                                  db.Column('concept_list_id', db.Integer, db.ForeignKey('concept_lists.id')),
                                  db.Column('concept_id', db.Integer, db.ForeignKey('concepts.id')))

class ConceptList(db.Model):
    """ Represents a list of words to quiz """
    __tablename__ = 'concept_lists'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode())
    concepts = db.relationship("Concept", secondary=concept_list_concepts)