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
        def keyfunc(form):
            return (form.concept_id, form.language_id)
        results = self.formCls.query.filter(self.formCls.language_id.in_(self.languageIds), self.formCls.concept_id.in_(self.conceptIds)).all()
        return {keyfunc(result):result for result in results}
        
    def get(self, *, conceptId, languageId):
        """ Return the Concept Form for the given values """
        return self[(conceptId, languageId)]
        
    def getAll(self, *, conceptIds, languageId):
        """ Return the Concept Form for the given values """
        return [self[(conceptId, languageId)] for conceptId in conceptIds]