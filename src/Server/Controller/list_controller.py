from Server.helpers.admin_json_factory import toJson

from auth_json_controller import AuthJSONController

class ListController(AuthJSONController):
    """ Controller to return the list of all records for a particular model """
    
    def __init__(self, modelCls, routeParams={}):
        """ Initialize the List Controller """
        AuthJSONController.__init__(self)
        self.modelCls = modelCls
        self.routeParams = routeParams
    
    def performWithJSON(self, *args, **kwargs):
        """ Convert the records to JSON """
        json = kwargs['json']
        user = kwargs['user']
        query = self.modelCls.query.filter_by(**{self.routeParams[routeParam]:kwargs[routeParam] for routeParam in self.routeParams})
        return {"records":toJson(query.all(), user=user)}