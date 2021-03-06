from Data import ConceptPair, Language, LanguageEnrollment, Symbol, SymbolList, User, BoundConceptList, Word, WordList
from ..Quiz import QuizJson

from kao_json import JsonFactory, AsObj, ViaAttr, ViaFn

def MasteryAttr():
    def GetMateryRating(pair, masteryCache):
        """ Return the mastery rating for a Concept Pair """    
        return masteryCache[pair.foreign.id].rating
    return ViaFn(GetMateryRating, requires=['masteryCache'])
    
def HasLearned(form, learnedCache):
    """ Return if the user has learned the given form """
    return form.id in learnedCache

jsonFactory = JsonFactory({(Symbol, Word):AsObj(id=ViaAttr(), text=ViaAttr(), learned=ViaFn(HasLearned, requires=['learnedCache'])),
                           ConceptPair:AsObj(foreign=ViaAttr(), native=ViaAttr(), mastery=MasteryAttr()),
                           BoundConceptList:AsObj(id=ViaAttr(), name=ViaAttr(), concepts=ViaAttr()),
                           User:AsObj(id=ViaAttr(), email=ViaAttr(), is_admin=ViaAttr(), givenName=ViaAttr(), lastName=ViaAttr(), nativeLanguage=ViaAttr()),
                           Language:AsObj(id=ViaAttr(), name=ViaAttr()),
                           LanguageEnrollment:AsObj(id=ViaAttr(), language=ViaAttr(), default=ViaAttr())
                          }, QuizJson)

toJson = jsonFactory.toJson