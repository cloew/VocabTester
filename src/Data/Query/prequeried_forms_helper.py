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
        languageNeedsConcepts = {self.foreignLanguage:[], self.nativeLanguage:[]}
        for form in self.items:
            concept = Concept(id=form.concept_id)
            if form.language_id != self.foreignLanguage.id:
                languageNeedsConcepts[self.foreignLanguage].append(concept)
            else:
                languageNeedsConcepts[self.nativeLanguage].append(concept)
                
        nativeCache = self._buildCacheFor(self.nativeLanguage, languageNeedsConcepts[self.nativeLanguage])
        foreignCache = self._buildCacheFor(self.foreignLanguage, languageNeedsConcepts[self.foreignLanguage])
        nativeCache.add(self.items)
        nativeCache.add(foreignCache.results.values())
        return nativeCache
        
    def _buildCacheFor(self, language, concepts):
        """ Build the cache for the given language """
        return ConceptFormCache(self.modelCls, concepts, [language])
        
    @lazy_property
    def conceptManager(self):
        """ Return the Concept Manager """
        return ConceptManager(self.cache, self.nativeLanguage, self.foreignLanguage)
        
    def getConceptPairs(self):
        """ Return the learned Concept Pairs """
        return self.conceptManager.getConceptPairs([form.concept_id for form in self.items])