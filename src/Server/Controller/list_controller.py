from Server.helpers.admin_json_factory import toJson

from auth_json_controller import AuthJSONController

class ListController(AuthJSONController):
    """ Controller to return the list of all records for a particular model """
    
    def __init__(self, modelCls):
        """ Initialize the List Controller """
        AuthJSONController.__init__(self)
        self.modelCls = modelCls
    
    def performWithJSON(self, json=None, user=None):
        """ Convert the records to JSON """
        return {"records":toJson(self.modelCls.query.all(), user=user)}