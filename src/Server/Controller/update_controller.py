from Server.helpers.admin_json_factory import toJson

from auth_json_controller import AuthJSONController
from kao_flask.ext.sqlalchemy.database import db

class UpdateController(AuthJSONController):
    """ Controller to update a record for a particular model """
    
    def __init__(self, modelCls):
        """ Initialize the Update Controller """
        AuthJSONController.__init__(self)
        self.modelCls = modelCls
    
    def performWithJSON(self, id, json=None, user=None):
        """ Remove the record """
        record = self.modelCls.query.filter(self.modelCls.id==id).first()
        for key in json:
            setattr(record, key, json[key])
        db.session.add(record)
        db.session.commit()
        return {"record":toJson(record)}