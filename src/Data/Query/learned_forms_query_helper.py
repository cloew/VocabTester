from ..concept import Concept
from ..concept_manager import ConceptManager
from ..Cache import ConceptFormCache

from kao_decorators import lazy_property, proxy_for

@proxy_for('user', ['nativeLanguage'])
class LearnedFormsQueryHelper:
    """ Helper class to manage properly querying for Learned Forms """
    
    def __init__(self, user, modelCls, *, foreign):
        """ Initialize with the User, Model Class and the Foreign languages """
        self.user = user
        self.modelCls = modelCls
        self.foreignLanguage = foreign
        
    @lazy_property
    def items(self):
        """ Return all the Concept Lists """
        return self.user.getLearnedFor(self.modelCls, self.foreignLanguage)
        
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