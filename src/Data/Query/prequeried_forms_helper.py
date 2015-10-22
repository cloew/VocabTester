from ..concept import Concept
from ..concept_manager import ConceptManager
from ..Cache import ConceptFormCache

from kao_decorators import lazy_property

class PrequeriedFormsHelper:
    """ Helper class to manage properly querying for Learned Forms """
    
    def __init__(self, forms, formInfo, languages):
        """ Initialize with the initial Forms, Model Class and the Languages """
        self.items = forms
        self.formInfo = formInfo
        self.languages = languages
        
    @lazy_property
    def cache(self):
        """ Return the Concept Form Cache """
        languageNeedsConcepts = {self.languages.foreign:[], self.languages.native:[]}
        for form in self.items:
            concept = Concept(id=form.concept_id)
            if form.language_id != self.languages.foreign.id:
                languageNeedsConcepts[self.languages.foreign].append(concept)
            else:
                languageNeedsConcepts[self.languages.native].append(concept)
                
        nativeCache = self._buildCacheFor(self.languages.native, languageNeedsConcepts[self.languages.native])
        foreignCache = self._buildCacheFor(self.languages.foreign, languageNeedsConcepts[self.languages.foreign])
        nativeCache.add(self.items)
        nativeCache.add(foreignCache.results.values())
        return nativeCache
        
    def _buildCacheFor(self, language, concepts):
        """ Build the cache for the given language """
        return ConceptFormCache(self.formInfo.formModel, concepts, [language])
        
    @lazy_property
    def conceptManager(self):
        """ Return the Concept Manager """
        return ConceptManager(self.cache, self.languages)
        
    def getConceptPairs(self):
        """ Return the learned Concept Pairs """
        return self.conceptManager.getConceptPairs([form.concept_id for form in self.items])