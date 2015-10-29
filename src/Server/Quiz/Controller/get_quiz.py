from Server.auth import auth
from Server.helpers import BuildLanguageContext
from Server.helpers.json_factory import toJson

from Data import Language
from Data.Cache import BuildMasteryCache, LearnedCache
from Data.Query import ConceptListQueryHelper
from Quiz import Quiz

class GetQuiz(auth.JSONController):
    """ Controller to return the quiz """
    
    def __init__(self, formInfo):
        """ Initialize the Quiz Controller """
        auth.JSONController.__init__(self)
        self.formInfo = formInfo
    
    def performWithJSON(self, languageId, listId, json=None, user=None):
        """ Convert the quiz to JSON """
        languageContext = BuildLanguageContext(languageId, user)
        
        conceptListHelper = ConceptListQueryHelper(self.formInfo, self.formInfo.listModel.query.filter_by(id=listId), languageContext)
        userList = conceptListHelper.buildUserLists(user)[0]
        
        masteryCache = BuildMasteryCache.ViaPairs(userList.concepts, self.formInfo, user)
        learnedCache = LearnedCache(user, self.formInfo)
        quiz = Quiz(userList.name, userList.concepts, masteryCache)
        
        return {"quiz":toJson(quiz, user=user, learnedCache=learnedCache, masteryCache=masteryCache)}