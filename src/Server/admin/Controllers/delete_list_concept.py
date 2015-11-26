from ..concepts_to_json import ConceptsToJson
from Data import Concept
from Server.auth import auth
from Server.decorators import requires_admin

from kao_flask.controllers.json_controller import JSONController
from kao_flask.ext.sqlalchemy import db

class DeleteListConcept(JSONController):
    """ Controller to delete a List-Concept connection """
    
    def __init__(self, formInfo):
        """ Initialize the Controller """
        self.formInfo = formInfo
        JSONController.__init__(self, decorators=[auth.requires_auth, requires_admin])
    
    def performWithJSON(self, listId, conceptId, **kwargs):
        """ Convert the records to JSON """
        conceptList = self.formInfo.listModel.query.filter_by(id=listId).first()
        concept = Concept(id=conceptId)
        conceptList.concepts.remove(concept)
        
        db.session.add(conceptList)
        db.session.commit()
        
        return {"record":ConceptsToJson(conceptList, **kwargs)}