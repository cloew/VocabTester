from Server.helpers.admin_json_factory import toJson

from auth_json_controller import AuthJSONController

class RecordController(AuthJSONController):
    """ Controller to return the requested record for a particular model """
    
    def __init__(self, modelCls):
        """ Initialize the Record Controller """
        AuthJSONController.__init__(self)
        self.modelCls = modelCls
    
    def performWithJSON(self, id, json=None, user=None):
        """ Convert the records to JSON """
        return {"record":toJson(self.modelCls.query.filter(self.modelCls.id==id).first())}