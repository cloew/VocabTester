from kao_flask.ext.sqlalchemy import db

learned_symbols = db.Table('learned_symbols', db.Model.metadata,
                                  db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                                  db.Column('symbol_id', db.Integer, db.ForeignKey('symbols.id')))

learned_words = db.Table('learned_words', db.Model.metadata,
                                  db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                                  db.Column('word_id', db.Integer, db.ForeignKey('words.id')))