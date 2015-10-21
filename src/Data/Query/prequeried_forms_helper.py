from ..concept import Concept
from ..concept_manager import ConceptManager
from ..Cache import ConceptFormCache

from kao_decorators import lazy_property

class PrequeriedFormsHelper:
    """ Helper class to manage properly querying for Learned Forms """
    
    def __init__(self, forms, modelCls, *, foreign, native):
        """ Initialize with the initial Forms, Model Class and the Languages """
        self.items = forms
        self.modelCls = modelCls
        self.foreignLanguage = foreign
        self.nativeLanguage = native
        
    @lazy_property
    def cache(self):
        """ Return the Concept Form Cache """
        concepts = [Concept(id=form.concept_id) for form in self.items]
        cache = ConceptFormCache(self.modelCls, concepts, [self.nativeLanguage])
        cache.add(self.items)
        return cache
        
    @lazy_property
    def conceptManager(self):
        """ Return the Concept Manager """
        return ConceptManager(self.cache, self.nativeLanguage, self.foreignLanguage)
        
    def getConceptPairs(self):
        """ Return the learned Concept Pairs """
        return self.conceptManager.getConceptPairs([form.concept_id for form in self.items])