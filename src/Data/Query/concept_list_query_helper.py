from ..Concept import Concept, ConceptManager
from ..ConceptList import BoundConceptList, concept_list_concepts
from ..Cache import ConceptFormCache
from ..Mastery import Mastery, StalenessPeriod

from kao_decorators import lazy_property
from sqlalchemy.orm import subqueryload

class ConceptListQueryHelper:
    """ Helper class to manage properly querying for Concept Lists """
    
    def __init__(self, formInfo, user, query, languages):
        """ Initialize with the base query and the Language Context """
        self.formInfo = formInfo
        self.query = self.buildQuery(formInfo, user, query, languages)
        self.languages = languages
        
    @lazy_property
    def items(self):
        """ Return all the Concept Lists """
        return self.query.all()
        
    @lazy_property
    def cache(self):
        """ Return the Concept Form Cache """
        return ConceptFormCache(self.formInfo.formModel, self.concepts, self.languages)
        
    @lazy_property
    def conceptManager(self):
        """ Return the Concept Manager """
        return ConceptManager(self.cache, self.languages)
        
    @lazy_property
    def concepts(self):
        """ Return the Concepts """
        return [concept for conceptList in self.items for concept in conceptList.concepts]
        
    @lazy_property
    def foreignForms(self):
        """ Return the Foreign Forms """
        return self.conceptManager.getForeignForms([concept.id for concept in self.concepts])
        
    @lazy_property
    def bound_lists(self):
        """ Return the Bound Concept Lists """
        return [BoundConceptList(conceptList, self.conceptManager) for conceptList in self.items]
        
    def buildQuery(self, formInfo, user, query, languages):
        """ Build the query to properly query for the Lists and order them by their average mastery """
        return query.options(subqueryload('concepts'))\
                    .join(concept_list_concepts)\
                    .join(Concept)\
                    .join(formInfo.formModel, (formInfo.formModel.language_id == languages.foreign.id) & (formInfo.formModel.concept_id == Concept.id))\
                    .join(Mastery, (Mastery.user_id==user.id) & (getattr(Mastery, formInfo.masteryFieldName) == formInfo.formModel.id))\
                    .join(StalenessPeriod)\
                    .order_by(formInfo.listModel.averageRatingFor(user, languages.foreign))