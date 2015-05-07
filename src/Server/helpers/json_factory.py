from kao_json import JsonFactory, JsonAttr, FieldAttr, StaticAttr

from Data.concept_pair import ConceptPair
from Data.symbol import Symbol
from Data.symbol_list import SymbolList
from Data.user import User
from Data.user_concept_list import UserConceptList
from Data.word import Word
from Data.word_list import WordList

from Quiz.quiz import Quiz
from Quiz.Question.options_question import OptionsQuestion
from Quiz.Question.foreign_prompt_question import ForeignPromptQuestion

from Server.helpers.user_proxy import UserProxy

def answerUrl(question, user):
    """ Returns the mastery rating for the word and user """    
    return "/api/mastery/{0}/answer".format(question.subject.getMasteryForUser(user).id)
    
def IsWordsQuiz(quiz):
    """ Returns if the quiz is for words """    
    return len(quiz.questions) == 0 or quiz.questions[0].subject.foreign.__class__ is Word
    
def GetMateryRating(form, user):
    """ Return the mastery rating for the given form """    
    return form.getMastery(user).rating
    
def HasLearned(form, user):
    """ Return if the user has learned the given form """
    hasLearnedMethod = {Word: user.hasLearnedWord, Symbol: user.hasLearnedSymbol}
    return hasLearnedMethod[form.__class__](form)

jsonFactory = JsonFactory([
                           ([Symbol, Word],[FieldAttr('id'), JsonAttr('text', unicode), JsonAttr('mastery', GetMateryRating, args=["user"]), 
                                            JsonAttr('learned', HasLearned, args=["user"])]),
                           (ConceptPair,[FieldAttr('foreign'), FieldAttr('native')]),
                           ([SymbolList, WordList],[FieldAttr('id'), FieldAttr('name'), JsonAttr('concepts', lambda s, u: s.getConceptPairs(u), args=["user"])]),
                           (UserConceptList,[FieldAttr('id'), FieldAttr('name'), FieldAttr('concepts'), FieldAttr('averageMastery')]),
                           ([User, UserProxy], [FieldAttr('id'), FieldAttr('email'), FieldAttr('givenName'), FieldAttr('lastName')]),
                           (OptionsQuestion, [FieldAttr('subject'), FieldAttr('queryWord'), FieldAttr('options'), FieldAttr('answerIndex'), StaticAttr('questionType', 'options'), JsonAttr('answerUrl', answerUrl, args=["user"])]),
                           (ForeignPromptQuestion, [FieldAttr('subject'), FieldAttr('prompt'), FieldAttr('answer'), StaticAttr('questionType', 'prompt'), JsonAttr('answerUrl', answerUrl, args=["user"])]),
                           (Quiz, [FieldAttr('name'), FieldAttr('questions'), JsonAttr('isWords', IsWordsQuiz)])
                          ])
                         
def toJson(object, **kwargs):
    return jsonFactory.converterFor(object).toJson(**kwargs)