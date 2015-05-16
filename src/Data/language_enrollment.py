from kao_flask.ext.sqlalchemy.database import db

class LanguageEnrollment(db.Model):
    """ Represents a user's enrollment in a language """
    __tablename__ = 'language_enrollments'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    language = db.relationship("Language")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", backref="languageEnrollments")
    default = db.Column(db.Boolean, default=False)