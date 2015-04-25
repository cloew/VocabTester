from Server.helpers.admin_json_factory import toJson

from auth_json_controller import AuthJSONController
from kao_flask.ext.sqlalchemy.database import db

class DeleteController(AuthJSONController):
    """ Controller to delete a record for a particular model """
    
    def __init__(self, modelCls):
        """ Initialize the Delete Controller """
        AuthJSONController.__init__(self)
        self.modelCls = modelCls
    
    def performWithJSON(self, id, json=None, user=None):
        """ Remove the record """
        record = self.modelCls.query.filter(self.modelCls.id==id).first()
        db.session.delete(record)
        db.session.commit()
        return {}