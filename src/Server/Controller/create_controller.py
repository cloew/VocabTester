from Server.helpers.admin_json_factory import toJson

from auth_json_controller import AuthJSONController
from kao_flask.ext.sqlalchemy.database import db

class CreateController(AuthJSONController):
    """ Controller to create a new record for a particular model """
    
    def __init__(self, modelCls, routeParams={}):
        """ Initialize the Create Controller """
        AuthJSONController.__init__(self)
        self.modelCls = modelCls
        self.routeParams = routeParams
    
    def performWithJSON(self, **kwargs):
        """ Convert the records to JSON """
        json = kwargs['json']
        user = kwargs['user']
        
        recordValues = {self.routeParams[routeParam]:kwargs[routeParam] for routeParam in self.routeParams}
        recordValues.update(json)
        record = self.modelCls(**recordValues)
        
        db.session.add(record)
        db.session.commit()
        return {"record":toJson(record)}