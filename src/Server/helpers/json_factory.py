from Data import ConceptPair, Language, LanguageEnrollment, Symbol, SymbolList, User, UserConceptList, Word, WordList
from ..Quiz import QuizJson

from kao_json import JsonFactory, AsObj, ViaAttr

def GetMateryRating(context):
    """ Return the mastery rating for a Concept Pair """    
    return context.args.masteryCache[context.obj.foreign.id].rating
    
def HasLearned(context):
    """ Return if the user has learned the given form """
    return context.obj.id in context.args.learnedCache

jsonFactory = JsonFactory({(Symbol, Word):AsObj(id=ViaAttr(), text=ViaAttr(), learned=HasLearned),
                           ConceptPair:AsObj(foreign=ViaAttr(), native=ViaAttr(), mastery=GetMateryRating),
                           UserConceptList:AsObj(id=ViaAttr(), name=ViaAttr(), concepts=ViaAttr()),
                           User:AsObj(id=ViaAttr(), email=ViaAttr(), is_admin=ViaAttr(), givenName=ViaAttr(), lastName=ViaAttr(), nativeLanguage=ViaAttr()),
                           Language:AsObj(id=ViaAttr(), name=ViaAttr()),
                           LanguageEnrollment:AsObj(id=ViaAttr(), language=ViaAttr(), default=ViaAttr())
                          }, QuizJson)

toJson = jsonFactory.toJson