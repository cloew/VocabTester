from ..Concept import ConceptManager
from ..user_concept_list import UserConceptList
from ..Cache import ConceptFormCache

from kao_decorators import lazy_property
from sqlalchemy.orm import subqueryload

class ConceptListQueryHelper:
    """ Helper class to manage properly querying for Concept Lists """
    
    def __init__(self, formInfo, query, languages):
        """ Initialize with the base query and the Language Context """
        self.formInfo = formInfo
        self.query = query.options(subqueryload('concepts'))
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
        """ Return the Foreign Forms """
        return [concept for conceptList in self.items for concept in conceptList.concepts]
        
    @lazy_property
    def foreignForms(self):
        """ Return the Foreign Forms """
        return self.conceptManager.getForeignForms([concept.id for concept in self.concepts])
        
    def buildUserLists(self, user):
        """ Return the User Bound Concept Lists """
        return [UserConceptList(conceptList, user, self.conceptManager) for conceptList in self.items]