from Data.user_concept_list import UserConceptList
from Data.word_list import WordList

from Server.helpers.json_factory import toJson
from auth_json_controller import AuthJSONController

class ConceptListsController(AuthJSONController):
    """ Controller to return the concept lists """
    
    def __init__(self, listModel):
        """ Initialize the Concept Lists Controller """
        AuthJSONController.__init__(self)
        self.listModel = listModel
    
    def performWithJSON(self, json=None, user=None):
        """ Convert the existing Concept Lists to JSON """
        lists = self.listModel.query.all()
        userLists = [UserConceptList(l, user) for l in lists]
        return {"lists":toJson(userLists, user=user)}