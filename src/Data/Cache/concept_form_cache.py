from kao_decorators import lazy_property, proxy_for

@proxy_for('results', ['__iter__', '__contains__', '__len__', '__getitem__'])
class ConceptFormCache:
    """ Helper class to perform the queries for the proper forms of Concepts """
    
    def __init__(self, formCls, concepts, languages):
        """ Initialize with the concepts and languages to request """
        self.formCls = formCls
        self.conceptIds = [concept.id for concept in concepts]
        self.languageIds = [language.id for language in languages]
        
    @lazy_property
    def results(self):
        """ Return the results """
        results = self.formCls.query.filter(self.formCls.language_id.in_(self.languageIds), self.formCls.concept_id.in_(self.conceptIds)).all()
        return self._buildResultsDictionary(results)
        
    def _buildResultsDictionary(self, results):
        """ Return the results dictionary """
        return {self.getKey(result):result for result in results}
        
    def add(self, conceptForms):
        """ Add the given forms to the results """
        self.results.extend(self._buildResultsDictionary(conceptForms))
        
    def get(self, *, conceptId, languageId):
        """ Return the Concept Form for the given values """
        return self[self.getIdKey(concetpId=conceptId, languageId=languageId)]
        
    def getAll(self, *, conceptIds, languageId):
        """ Return the Concept Form for the given values """
        return [self[self.getIdKey(conceptId=conceptId, languageId=languageId)] for conceptId in conceptIds]
        
    def getKey(self, form):
        """ Return the key for the given form """
        return self.getIdKey(conceptId=form.concept_id, languageId=form.language_id)
        
    def getIdKey(self, *, conceptId, languageId):
        """ Return the key for the given form """
        return (conceptId, languageId)