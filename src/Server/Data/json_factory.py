from kao_json import JsonFactory, JsonAttr, FieldAttr

from Data.concept_pair import ConceptPair
from Data.user import User
from Data.word import Word
from Data.word_list import WordList

from Quiz.quiz import Quiz
from Quiz.Question.question import Question

from Server.Data.user_proxy import UserProxy

def answerUrl(question, user):
    """ Returns the mastery rating for the word and user """    
    return "/api/mastery/{0}/answer".format(question.subject.getMasteryForUser(user).id)

jsonFactory = JsonFactory([
                           (Word,[FieldAttr('id'), JsonAttr('text', unicode), JsonAttr('mastery', Word.getMasteryRating, args=["user"])]),
                           (ConceptPair,[FieldAttr('foreign'), FieldAttr('native')]),
                           (WordList,[FieldAttr('id'), FieldAttr('name'), JsonAttr('concepts', WordList.getWordPairs, args=["conceptManager"])]),
                           ([User, UserProxy], [FieldAttr('id'), FieldAttr('email'), FieldAttr('givenName'), FieldAttr('lastName')]),
                           (Question, [FieldAttr('subject'), FieldAttr('queryWord'), FieldAttr('options'), FieldAttr('answerIndex'), JsonAttr('answerUrl', answerUrl, args=["user"])]),
                           (Quiz,[FieldAttr('name', field='wordList.name'), FieldAttr('questions')])
                          ])
                         
def toJson(object, **kwargs):
    return jsonFactory.converterFor(object).toJson(**kwargs)