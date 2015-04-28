from kao_json import JsonFactory, JsonAttr, FieldAttr

from Data.concept import Concept
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

def GetNativeForm(concept, user):
    """ Return the native form of the concept """
    form = Word.query.filter_by(concept_id=concept.id, language_id=user.nativeLanguage.id).first()
    if form is None:
        form = Symbol.query.filter_by(concept_id=concept.id, language_id=user.nativeLanguage.id).first()
    return form.text if form is not None else ''

jsonFactory = JsonFactory([(Concept, [FieldAttr('id'), JsonAttr('native', GetNativeForm, args=["user"])]),
                           ([Symbol, Word], [FieldAttr('id'), JsonAttr('text', unicode), FieldAttr('language')]),
                           (ConceptPair, [FieldAttr('foreign'), FieldAttr('native')]),
                           (Language, [FieldAttr('id'), FieldAttr('name')])
                          ])
                         
def toJson(object, **kwargs):
    return jsonFactory.converterFor(object).toJson(**kwargs)