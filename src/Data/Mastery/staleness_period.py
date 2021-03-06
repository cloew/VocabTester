from kao_flask.ext.sqlalchemy import db

class StalenessPeriod(db.Model):
    """ Represents a staleness period """
    __tablename__ = 'staleness_periods'
    
    id = db.Column(db.Integer, primary_key=True)
    days = db.Column(db.Integer)
    first = db.Column(db.Boolean, default=False)
    next_id = db.Column(db.Integer, db.ForeignKey('staleness_periods.id'))
    next = db.relationship("StalenessPeriod", remote_side=[id])
    
    @classmethod
    def getFirstStalenessPeriod(cls):
        """ Return the first staleness period """
        return cls.query.filter_by(first=True).first()