from Data import ConceptPair, Language, LanguageEnrollment, Symbol, SymbolList, User, UserConceptList, Word, WordList
from ..Quiz import QuizJson
from kao_json import JsonFactory, JsonAttr, FieldAttr, StaticAttr

def GetMateryRating(form, user):
    """ Return the mastery rating for the given form """    
    return form.getMastery(user).rating
    
def HasLearned(form, user):
    """ Return if the user has learned the given form """
    hasLearnedMethod = {Word: user.hasLearnedWord, Symbol: user.hasLearnedSymbol}
    return hasLearnedMethod[form.__class__](form)

jsonFactory = JsonFactory([
                           ([Symbol, Word],[FieldAttr('id'), FieldAttr('text'), JsonAttr('mastery', GetMateryRating, args=["user"]), 
                                            JsonAttr('learned', HasLearned, args=["user"])]),
                           (ConceptPair,[FieldAttr('foreign'), FieldAttr('native')]),
                           ([SymbolList, WordList],[FieldAttr('id'), FieldAttr('name'), JsonAttr('concepts', lambda s, u: s.getConceptPairs(u), args=["user"])]),
                           (UserConceptList,[FieldAttr('id'), FieldAttr('name'), FieldAttr('concepts'), FieldAttr('averageMastery')]),
                           ([User], [FieldAttr('id'), FieldAttr('email'), FieldAttr('is_admin'), FieldAttr('givenName'), FieldAttr('lastName'), FieldAttr('nativeLanguage')]),
                           (Language, [FieldAttr('id'), FieldAttr('name')]),
                           (LanguageEnrollment, [FieldAttr('id'), FieldAttr('language'), FieldAttr('default')])
                          ] + QuizJson)
                         
def toJson(object, **kwargs):
    return jsonFactory.converterFor(object).toJson(**kwargs)