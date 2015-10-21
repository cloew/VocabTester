from Server.auth import auth
from Server.helpers.json_factory import toJson

from Data import Language
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
        foreignLanguage = Language(id=languageId)
        nativeLanguage = Language(id=user.native_language_id)
        
        conceptListHelper = ConceptListQueryHelper(self.listModel, self.listModel.query.filter_by(id=listId), native=nativeLanguage, foreign=foreignLanguage)
        userList = conceptListHelper.buildUserLists(user)[0]
        
        quiz = Quiz(userList.name, userList.concepts, user)
        return {"quiz":toJson(quiz, user=user)}