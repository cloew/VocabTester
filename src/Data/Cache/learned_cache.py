from kao_decorators import lazy_property, proxy_for
from kao_flask.ext.sqlalchemy import db

@proxy_for('results', ['__contains__'])
class LearnedCache:
    """ Helper class to manage whether Forms have bee learned """
    
    def __init__(self, user, formInfo):
        """ Initialize with the User and Form Info """
        self.user = user
        self.table = formInfo.learnedTable
        
    @lazy_property
    def results(self):
        """ Return the results """
        results = db.session.query(self.table).filter_by(user_id=user.id).all()
        return {form_id for user_id, form_id in results}