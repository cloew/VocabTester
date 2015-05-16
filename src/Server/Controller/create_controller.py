from Server.helpers.admin_json_factory import toJson
from Server.helpers.record_value_provider import RecordValueProvider

from auth_json_controller import AuthJSONController
from kao_flask.ext.sqlalchemy.database import db
from smart_defaults import smart_defaults, EvenIfNone

class CreateController(AuthJSONController):
    """ Controller to create a new record for a particular model """
    
    @smart_defaults
    def __init__(self, modelCls, routeParams={}, recordValueProvider=EvenIfNone(RecordValueProvider())):
        """ Initialize the Create Controller """
        AuthJSONController.__init__(self)
        self.modelCls = modelCls
        self.routeParams = routeParams
        self.recordValueProvider = recordValueProvider
    
    def performWithJSON(self, **kwargs):
        """ Convert the records to JSON """
        json = kwargs['json']
        
        recordValues = {self.routeParams[routeParam]:kwargs[routeParam] for routeParam in self.routeParams}
        providedRecordValues = self.recordValueProvider.getRecordValues(json)
        recordValues.update(providedRecordValues)
        record = self.modelCls(**recordValues)
        
        db.session.add(record)
        db.session.commit()
        return {"record":toJson(record)}
        