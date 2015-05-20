from Server.helpers.admin_json_factory import toJson
from kao_flask.controllers.json_controller import JSONController

class RecordController(JSONController):
    """ Controller to return the requested record for a particular model """
    
    def __init__(self, modelCls, decorators=[]):
        """ Initialize the Record Controller """
        JSONController.__init__(self, decorators=decorators)
        self.modelCls = modelCls
    
    def performWithJSON(self, id, **kwargs):
        """ Convert the records to JSON """
        json = kwargs['json']
        user = kwargs['user']
        return {"record":toJson(self.modelCls.query.filter(self.modelCls.id==id).first(), user=user)}