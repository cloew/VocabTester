from .symbol_route_info import SymbolRouteInfo
from .word_route_info import WordRouteInfo

from kao_decorators import lazy_property, proxy_for
from kao_flask import Endpoint, Routes

@proxy_for('_routes', ['register'])
class FormEndpoint:
    """ Helper class to provide the Endpoints for both Symbol and Word Concept Forms """
    routeInfos = [SymbolRouteInfo, WordRouteInfo]
             
    def __init__(self, url, **methodToController):
        """ Initialize with the url and Method To Controller Dictionary """
        self.url = url
        self.methodToController = methodToController
        
    @lazy_property
    def _routes(self):
        """ Return the underlying routes """
        routes = Routes()
        for routeInfo in self.routeInfos:
            cleanedUrl = self.url.format(form=routeInfo.form, formList=routeInfo.formList)
            viewFns = {method:cls(routeInfo.info) for method, cls in self.methodToController.items()}
            routes.add(Endpoint(cleanedUrl, **viewFns))
        return routes