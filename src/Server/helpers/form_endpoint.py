from .symbol_route_info import SymbolRouteInfo
from .word_route_info import WordRouteInfo

from kao_decorators import lazy_property
from kao_flask import Endpoint

class FormEndpoint:
    """ Helper class to provide the Endpoints for both Symbol and Word Concept Forms """
    routeInfos = [SymbolRouteInfo, WordRouteInfo]
             
    def __init__(self, url, **methodToController):
        """ Initialize with the url and Method To Controller Dictionary """
        self.url = url
        self.methodToController = methodToController
        
    @lazy_property
    def endpoints(self):
        """ Return the underlying endpoints """
        return [Endpoint(self.url.format(form=routeInfo.form, formList=routeInfo.formList), **{method:cls(routeInfo.info) for method, cls in self.methodToController.items()}) for routeInfo in self.routeInfos]
        
    def register(self, app):
        """ Register the endpoints with the given app """
        for endpoint in self.endpoints:
            endpoint.register(app)