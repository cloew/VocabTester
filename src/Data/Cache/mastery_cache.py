from ..mastery import Mastery
from ..symbol import Symbol
from ..word import Word

from kao_decorators import proxy_for, lazy_property
from kao_flask.ext.sqlalchemy import db

@proxy_for('results', ['__iter__', '__contains__', '__len__'])
class MasteryCache:
    """ Helper class to request all the relevant Masteries """
    mastery_fields = {Symbol: 'symbol_id', Word:'word_id'}
    
    def __init__(self, forms, formCls, user):
        """ Initialize with the Concept Forms and User """
        self.forms = forms
        self.formCls = formCls
        self.user = user
        
    @lazy_property
    def results(self):
        """ Return the Masteries """
        items = self.loadMasteries()
        results = {getattr(item, self.masteryFieldName):item for item in items}
        return results
        
    def loadMasteries(self):
        """ Load the Masteries """
        if len(self.forms) > 0:
            masteryField = getattr(Mastery, self.masteryFieldName)
            formIds = [form.id for form in self.forms]
            return Mastery.query.filter_by(user_id=self.user.id).filter(masteryField.in_(formIds)).all()
        else:
            return []
        
    @lazy_property
    def masteryFieldName(self):
        """ Return the mastery field name to use """
        return self.mastery_fields[self.formCls]
            
    def __getitem__(self, formId):
        """ Return the proper Mastery record """
        if formId not in self:
            kwargs = {'user':self.user, self.masteryFieldName:formId}
            mastery = Mastery(**kwargs)
            db.session.add(mastery)
            db.session.commit()
            self.results[formId] = mastery
            
        return self.results[formId]