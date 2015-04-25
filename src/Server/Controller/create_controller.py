from Server.helpers.admin_json_factory import toJson

from auth_json_controller import AuthJSONController
from kao_flask.ext.sqlalchemy.database import db

class CreateController(AuthJSONController):
    """ Controller to create a new record for a particular model """
    
    def __init__(self, modelCls):
        """ Initialize the Create Controller """
        AuthJSONController.__init__(self)
        self.modelCls = modelCls
    
    def performWithJSON(self, json=None, user=None):
        """ Convert the records to JSON """
        record = self.modelCls(**json)
        db.session.add(record)
        db.session.commit()
        return {"record":toJson(record)}