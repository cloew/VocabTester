from Data import Concept, ConceptPair, Language, LanguageEnrollment, Symbol, User, Word
from kao_json import JsonFactory, JsonAttr, FieldAttr

def GetNativeForm(concept, user):
    """ Return the native form of the concept """
    form = Word.query.filter_by(concept_id=concept.id, language_id=user.nativeLanguage.id).first()
    if form is None:
        form = Symbol.query.filter_by(concept_id=concept.id, language_id=user.nativeLanguage.id).first()
    return form.text if form is not None else ''

jsonFactory = JsonFactory([(Concept, [FieldAttr('id'), JsonAttr('native', GetNativeForm, args=["user"])]),
                           ([Symbol, Word], [FieldAttr('id'), FieldAttr('text'), FieldAttr('language')]),
                           (ConceptPair, [FieldAttr('foreign'), FieldAttr('native')]),
                           ([User], [FieldAttr('id'), FieldAttr('email'), FieldAttr('is_admin'), FieldAttr('givenName'), FieldAttr('lastName'), FieldAttr('nativeLanguage')]),
                           (Language, [FieldAttr('id'), FieldAttr('name')]),
                           (LanguageEnrollment, [FieldAttr('id'), FieldAttr('language'), FieldAttr('default')])
                          ])
                         
def toJson(object, **kwargs):
    return jsonFactory.converterFor(object).toJson(**kwargs)