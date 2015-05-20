from Server.helpers.admin_json_factory import toJson
from Server.helpers.record_value_provider import RecordValueProvider

from kao_flask.controllers.json_controller import JSONController
from kao_flask.ext.sqlalchemy.database import db
from smart_defaults import smart_defaults, EvenIfNone

class UpdateController(JSONController):
    """ Controller to update a record for a particular model """
    
    @smart_defaults
    def __init__(self, modelCls, recordValueProvider=EvenIfNone(RecordValueProvider()), decorators=[]):
        """ Initialize the Update Controller """
        JSONController.__init__(self, decorators=decorators)
        self.modelCls = modelCls
        self.recordValueProvider = recordValueProvider
    
    def performWithJSON(self, id, **kwargs):
        """ Remove the record """
        json = kwargs['json']
        record = self.update(id, json)
        return {"record":toJson(record)}
        
    def update(self, id, json):
        """ Update the record """
        record = self.modelCls.query.filter(self.modelCls.id==id).first()
        recordValues = self.recordValueProvider.getRecordValues(json)
        for key in recordValues:
            setattr(record, key, recordValues[key])
            
        db.session.add(record)
        db.session.commit()
        return record