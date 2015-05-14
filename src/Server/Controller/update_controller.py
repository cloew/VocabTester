from Server.helpers.admin_json_factory import toJson
from Server.helpers.record_value_provider import RecordValueProvider

from auth_json_controller import AuthJSONController
from kao_flask.ext.sqlalchemy.database import db
from smart_defaults import smart_defaults, EvenIfNone

class UpdateController(AuthJSONController):
    """ Controller to update a record for a particular model """
    
    @smart_defaults
    def __init__(self, modelCls, recordValueProvider=EvenIfNone(RecordValueProvider())):
        """ Initialize the Update Controller """
        AuthJSONController.__init__(self)
        self.modelCls = modelCls
        self.recordValueProvider = recordValueProvider
    
    def performWithJSON(self, id, **kwargs):
        """ Remove the record """
        json = kwargs['json']
        user = kwargs['user']
        record = self.update(id, json, user)
        return {"record":toJson(record)}
        
    def update(self, id, json, user):
        """ Update the record """
        record = self.modelCls.query.filter(self.modelCls.id==id).first()
        recordValues = self.recordValueProvider.getRecordValues(json)
        for key in recordValues:
            setattr(record, key, recordValues[key])
            
        db.session.add(record)
        db.session.commit()
        return record