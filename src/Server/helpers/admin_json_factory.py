from kao_json import JsonFactory, JsonAttr, FieldAttr

from Data.concept_pair import ConceptPair
from Data.language import Language
from Data.symbol import Symbol
from Data.symbol_list import SymbolList
from Data.user import User
from Data.user_concept_list import UserConceptList
from Data.word import Word
from Data.word_list import WordList

from Quiz.quiz import Quiz
from Quiz.Question.question import Question

from Server.helpers.user_proxy import UserProxy

jsonFactory = JsonFactory([
                           ([Symbol, Word], [FieldAttr('id'), JsonAttr('text', unicode)]),
                           (ConceptPair, [FieldAttr('foreign'), FieldAttr('native')]),
                           (Language, [FieldAttr('id'), FieldAttr('name')])
                          ])
                         
def toJson(object, **kwargs):
    return jsonFactory.converterFor(object).toJson(**kwargs)