from Data import ConceptPair, Language, LanguageEnrollment, Symbol, SymbolList, User, UserConceptList, Word, WordList
from ..Quiz import QuizJson
from kao_json import JsonFactory, JsonAttr, FieldAttr, StaticAttr

def GetMateryRating(conceptPair, masteryCache):
    """ Return the mastery rating for the given form """    
    return masteryCache[conceptPair.foreign.id].rating
    
def HasLearned(form, learnedCache):
    """ Return if the user has learned the given form """
    return form.id in learnedCache

jsonFactory = JsonFactory([
                           ([Symbol, Word],[FieldAttr('id'), FieldAttr('text'), 
                                            JsonAttr('learned', HasLearned, args=["learnedCache"])]),
                           (ConceptPair,[FieldAttr('foreign'), FieldAttr('native'), JsonAttr('mastery', GetMateryRating, args=["masteryCache"])]),
                           (UserConceptList,[FieldAttr('id'), FieldAttr('name'), FieldAttr('concepts')]),
                           ([User], [FieldAttr('id'), FieldAttr('email'), FieldAttr('is_admin'), FieldAttr('givenName'), FieldAttr('lastName'), FieldAttr('nativeLanguage')]),
                           (Language, [FieldAttr('id'), FieldAttr('name')]),
                           (LanguageEnrollment, [FieldAttr('id'), FieldAttr('language'), FieldAttr('default')])
                          ] + QuizJson)
                         
def toJson(object, **kwargs):
    return jsonFactory.converterFor(object).toJson(**kwargs)