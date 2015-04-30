from Server.Controller.create_controller import CreateController
from Server.Controller.delete_controller import DeleteController
from Server.Controller.list_controller import ListController
from Server.Controller.record_controller import RecordController
from Server.Controller.update_controller import UpdateController

from Server.helpers.record_value_provider import RecordValueProvider

from kao_flask.endpoint import Endpoint

class CrudEndpoints:
    """ Represents the standard CRUD Endpoints for a particualr model class """
    
    def __init__(self, rootUrl, modelCls, routeParams={}, jsonColumnMap={}):
        """ Initialize with the root URL and the model class to wrap """
        recordValueProvider = RecordValueProvider(jsonColumnMap)
        self.listEndpoint = Endpoint(rootUrl, get=ListController(modelCls, routeParams=routeParams), 
                                              post=CreateController(modelCls, routeParams=routeParams, recordValueProvider=recordValueProvider))
        self.recordEndpoint = Endpoint(rootUrl+'/<int:id>', get=RecordController(modelCls), 
                                                            put=UpdateController(modelCls, recordValueProvider=recordValueProvider), 
                                                            delete=DeleteController(modelCls))
        
    @property
    def endpoints(self):
        """ Return the endpoints """
        return [self.listEndpoint, self.recordEndpoint]