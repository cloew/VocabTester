from kao_flask.ext.sqlalchemy.database import db

from Data.answer import Answer
from Data.mastery import Mastery

def answer(user, word, correct):
    """ Add an answer to the word if its correct """
    mastery = user.getMastery(word)
    if len(mastery.answers) >= Mastery.MAX_ANSWERS:
        db.session.delete(mastery.answers[0])
        db.session.commit()
    CreateAnswer(mastery, correct)

def GetWordMastery(user, word):
    """ Return the word mastery for the word and user """
    return mastery
    
def CreateAnswer(mastery, correct):
    """ Create an answer for the mastery """
    answer = Answer(correct=correct, mastery=mastery)
    db.session.add(answer)
    db.session.commit()