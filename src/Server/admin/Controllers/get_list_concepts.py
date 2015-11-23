from ..concepts_to_json import ConceptsToJson
from Server.auth import auth
from Server.decorators import requires_admin

from kao_flask.controllers.json_controller import JSONController

class GetListConcepts(JSONController):
    """ Controller to return the list of concepts for a list """
    
    def __init__(self, formInfo):
        """ Initialize the List Controller """
        self.formInfo = formInfo
        JSONController.__init__(self, decorators=[auth.requires_auth, requires_admin])
    
    def performWithJSON(self, listId, **kwargs):
        """ Convert the records to JSON """
        conceptLists = self.formInfo.listModel.query.filter_by(id=listId).all()
        return {"records":ConceptsToJson(conceptLists, **kwargs)}