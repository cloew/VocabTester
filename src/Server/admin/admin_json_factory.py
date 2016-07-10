from . import urls
from Data import Concept, ConceptList, ConceptPair, Language, LanguageEnrollment, Symbol, User, Word
from kao_json import JsonFactory, AsObj, ViaAttr, ViaFn

def GetConceptsUrl(context):
    """ Return the proper concepts url """
    conceptList = context.obj
    if conceptList.isWords:
        return urls.WordListConcepts.build(listId=conceptList.id)
    else:
        return urls.SymbolListConcepts.build(listId=conceptList.id)

def GetNativeForm(concept, symbolCache, wordCache, user):
    """ Return the native form of the concept """
    key = symbolCache.getIdKey(conceptId=concept.id, languageId=user.nativeLanguage.id)
    if key in symbolCache:
        return symbolCache[key].text
    elif key in wordCache:
        return wordCache[key].text
    return ''

jsonFactory = JsonFactory({Concept:AsObj(id=ViaAttr(), native=ViaFn(GetNativeForm, requires=['symbolCache', 'wordCache', 'user'])),
                           (Symbol, Word):AsObj(id=ViaAttr(), text=ViaAttr(), language=ViaAttr()),
                           ConceptList:AsObj(id=ViaAttr(), name=ViaAttr(), isWords=ViaAttr(), conceptsUrl=GetConceptsUrl),
                           ConceptPair:AsObj(foreign=ViaAttr(), native=ViaAttr()),
                           User:AsObj(id=ViaAttr(), email=ViaAttr(), is_admin=ViaAttr(), givenName=ViaAttr(), lastName=ViaAttr(), nativeLanguage=ViaAttr()),
                           Language:AsObj(id=ViaAttr(), name=ViaAttr()),
                           LanguageEnrollment:AsObj(id=ViaAttr(), language=ViaAttr(), default=ViaAttr())
                          })
                         
toJson = jsonFactory.toJson