from Server.auth import auth
from Server.helpers import BuildLanguageContext
from Server.helpers.json_factory import toJson

from Data import Language
from Data.Cache import MasteryCache
from Data.Query import ConceptListQueryHelper
from Quiz import Quiz

class GetQuiz(auth.JSONController):
    """ Controller to return the quiz """
    
    def __init__(self, listModel):
        """ Initialize the Quiz Controller """
        auth.JSONController.__init__(self)
        self.listModel = listModel
    
    def performWithJSON(self, languageId, listId, json=None, user=None):
        """ Convert the quiz to JSON """
        languageContext = BuildLanguageContext(languageId, user)
        
        conceptListHelper = ConceptListQueryHelper(self.listModel, self.listModel.query.filter_by(id=listId), languageContext)
        userList = conceptListHelper.buildUserLists(user)[0]
        
        masteryCache = MasteryCache([pair.foreign for pair in userList.concepts], self.listModel.conceptFormCls, user)
        quiz = Quiz(userList.name, userList.concepts, masteryCache)
        
        return {"quiz":toJson(quiz, user=user, masteryCache=masteryCache)}