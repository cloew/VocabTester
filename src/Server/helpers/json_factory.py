from kao_json import JsonFactory, JsonAttr, FieldAttr

from Data.concept_pair import ConceptPair
from Data.symbol import Symbol
from Data.symbol_list import SymbolList
from Data.user import User
from Data.word import Word
from Data.word_list import WordList

from Quiz.quiz import Quiz
from Quiz.Question.question import Question

from Server.helpers.user_proxy import UserProxy

def answerUrl(question, user):
    """ Returns the mastery rating for the word and user """    
    return "/api/mastery/{0}/answer".format(question.subject.getMasteryForUser(user).id)

jsonFactory = JsonFactory([
                           ([Symbol, Word],[FieldAttr('id'), JsonAttr('text', unicode), JsonAttr('mastery', lambda s, u: s.getMasteryRating(u), args=["user"])]),
                           (ConceptPair,[FieldAttr('foreign'), FieldAttr('native')]),
                           ([SymbolList, WordList],[FieldAttr('id'), FieldAttr('name'), JsonAttr('concepts', lambda s, u: s.getConceptPairs(u), args=["user"])]),
                           ([User, UserProxy], [FieldAttr('id'), FieldAttr('email'), FieldAttr('givenName'), FieldAttr('lastName')]),
                           (Question, [FieldAttr('subject'), FieldAttr('queryWord'), FieldAttr('options'), FieldAttr('answerIndex'), JsonAttr('answerUrl', answerUrl, args=["user"])]),
                           (Quiz, [FieldAttr('name', field='wordList.name'), FieldAttr('questions')])
                          ])
                         
def toJson(object, **kwargs):
    return jsonFactory.converterFor(object).toJson(**kwargs)