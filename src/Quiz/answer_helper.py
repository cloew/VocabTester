from kao_flask.database import db

from Data.word_mastery import WordMastery
from Data.word_answer import WordAnswer

def Answer(word, correct):
    """ Add an answer to the word if its correct """
    mastery = GetWordMastery(word)
    if len(mastery.answers) >= WordMastery.MAX_ANSWERS:
        mastery.remove(mastery.answers[0])
    CreateAnswer(mastery, correct)

def GetWordMastery(word):
    """ Return the word mastery for the word """
    if word.mastery is None:
        mastery = WordMastery(word=word)
        db.session.add(mastery)
        db.session.commit()
    else:
        mastery = word.mastery
    
    return mastery
    
def CreateAnswer(mastery, correct):
    """ Create an answer for the mastery """
    answer = WordAnswer(correct=correct, word_mastery=mastery)
    db.session.add(answer)
    db.session.commit()