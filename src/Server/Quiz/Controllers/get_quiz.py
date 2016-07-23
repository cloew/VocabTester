from Server.auth import auth
from Server.helpers import BuildLearningContext
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
        learningContext = BuildLearningContext(languageId, user)
        languageContext = learningContext.languageContext
        
        conceptListHelper = ConceptListQueryHelper(self.formInfo, user, self.formInfo.listModel.query.filter_by(id=listId), languageContext)
        boundList = conceptListHelper.bound_lists[0]
        
        masteryCache = BuildMasteryCache.ViaPairs(boundList.concepts, self.formInfo, user)
        learnedCache = LearnedCache(user, self.formInfo)
        quiz = Quiz(boundList.name, boundList.concepts, masteryCache)
        
        return {"quiz":toJson(quiz, user=user, learnedCache=learnedCache, masteryCache=masteryCache)}