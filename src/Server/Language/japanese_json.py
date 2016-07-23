from Language.Japanese import WordData
from kao_json import AsObj, ViaAttr, ViaFn

def UserTextAttr():
    def GetUserText(data, learningContext):
        """ Return the mastery rating for a Concept Pair """
        if learningContext.isForeign(data.word):
            textConverter = learningContext.foreignLearningData.textConverter
            return data.getUserText(textConverter)
        else:
            return None
    return ViaFn(GetUserText, requires=['learningContext'])
    
def HasLearned(form, learnedCache):
    """ Return if the user has learned the given form """
    return form.id in learnedCache

JapaneseJson = {
    WordData:AsObj(readings=ViaAttr(), user_text=UserTextAttr())
}