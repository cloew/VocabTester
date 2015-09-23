from ..auth import auth
from ..helpers.json_factory import toJson
from Data import Language, UserConceptList

class ConceptListsController(auth.JSONController):
    """ Controller to return the concept lists """
    
    def __init__(self, listModel):
        """ Initialize the Concept Lists Controller """
        auth.JSONController.__init__(self)
        self.listModel = listModel
    
    def performWithJSON(self, languageId, json=None, user=None):
        """ Convert the existing Concept Lists to JSON """
        language = Language(id=languageId)
        conceptLists = self.listModel.query.all()
        userLists = [UserConceptList(conceptList, user, language) for conceptList in conceptLists]
        return {"lists":toJson([userList for userList in userLists if len(userList.concepts) > 0], user=user)}