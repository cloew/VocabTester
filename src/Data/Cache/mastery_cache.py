from ..mastery import Mastery
from ..symbol import Symbol
from ..word import Word

from kao_decorators import lazy_property

@proxy_for('results', ['__iter__', '__contains__', '__len__', '__getitem__'])
class MasteryCache:
    """ Helper class to request all the relevant Masteries """
    mastery_fields = {Symbol: 'symbol_id', Word:'word_id'}
    
    def __init__(self, forms, user):
        """ Initialize with the Concept Forms and User """
        self.forms = forms
        self.user = user
        
    @lazy_property
    def results(self):
        """ Return the Masteries """
        items = self.loadMasteries()
        return {getattr(item, self.masteryFieldName):item for item in items}
        
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
        """ Return the amstery field name to use """
        if len(self.forms) > 0:
            return self.mastery_fields[self.forms[0].__class__]
        else:
            return None