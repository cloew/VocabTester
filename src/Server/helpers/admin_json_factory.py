from Data import Concept, ConceptPair, Language, LanguageEnrollment, Symbol, User, Word
from kao_json import JsonFactory, AsObj, ViaAttr, ViaFn

def GetNativeForm(concept, user):
    """ Return the native form of the concept """
    form = Word.query.filter_by(concept_id=concept.id, language_id=user.nativeLanguage.id).first()
    if form is None:
        form = Symbol.query.filter_by(concept_id=concept.id, language_id=user.nativeLanguage.id).first()
    return form.text if form is not None else ''

jsonFactory = JsonFactory({Concept:AsObj(id=ViaAttr(), native=ViaFn(GetNativeForm, requires=['user'])),
                           (Symbol, Word):AsObj(id=ViaAttr(), text=ViaAttr(), language=ViaAttr()),
                           ConceptPair:AsObj(foreign=ViaAttr(), native=ViaAttr()),
                           User:AsObj(id=ViaAttr(), email=ViaAttr(), is_admin=ViaAttr(), givenName=ViaAttr(), lastName=ViaAttr(), nativeLanguage=ViaAttr()),
                           Language:AsObj(id=ViaAttr(), name=ViaAttr()),
                           LanguageEnrollment:AsObj(id=ViaAttr(), language=ViaAttr(), default=ViaAttr())
                          })
                         
toJson = jsonFactory.toJson