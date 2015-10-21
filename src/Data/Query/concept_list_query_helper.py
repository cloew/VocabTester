from ..concept_manager import ConceptManager
from ..user_concept_list import UserConceptList
from ..Cache import ConceptFormCache

from kao_decorators import lazy_property
from sqlalchemy.orm import subqueryload

class ConceptListQueryHelper:
    """ Helper class to manage properly querying for Concept Lists """
    
    def __init__(self, listModelCls, query, *, native, foreign):
        """ Initialize with the base query and the native and foreign languages """
        self.listModelCls = listModelCls
        self.query = query.options(subqueryload('concepts'))
        self.nativeLanguage = native
        self.foreignLanguage = foreign
        
    @lazy_property
    def items(self):
        """ Return all the Concept Lists """
        return self.query.all()
        
    @lazy_property
    def cache(self):
        """ Return the Concept Form Cache """
        concepts = [concept for conceptList in self.items for concept in conceptList.concepts]
        return ConceptFormCache(self.listModelCls.conceptFormCls, concepts, [self.nativeLanguage, self.foreignLanguage])
        
    @lazy_property
    def conceptManager(self):
        """ Return the Concept Manager """
        return ConceptManager(self.cache, self.nativeLanguage, self.foreignLanguage)
        
    def buildUserLists(self, user):
        """ Return the User Bound Concept Lists """
        return [UserConceptList(conceptList, user, self.conceptManager) for conceptList in self.items]