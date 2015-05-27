from Server.helpers.admin_json_factory import toJson

from kao_flask.controllers.json_controller import JSONController
from kao_flask.ext.sqlalchemy.database import db

class DeleteController(JSONController):
    """ Controller to delete a record for a particular model """
    
    def __init__(self, modelCls, decorators=[]):
        """ Initialize the Delete Controller """
        JSONController.__init__(self, decorators=decorators)
        self.modelCls = modelCls
    
    def performWithJSON(self, id, **kwargs):
        """ Remove the record """
        json = kwargs['json']
        
        record = self.modelCls.query.filter(self.modelCls.id==id).first()
        db.session.delete(record)
        db.session.commit()
        return {}