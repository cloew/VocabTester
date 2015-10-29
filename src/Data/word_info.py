from .Concept import Word
from .ConceptList import WordList
from .learned_tables import learned_words

class WordInfo:
    """ Helper class to hold info regarding the Word Form """
    formModel = Word
    listModel = WordList
    masteryFieldName = 'word_id'
    learnedField = 'learnedWords'
    learnedTable = learned_words