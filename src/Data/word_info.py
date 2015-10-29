from .user import learned_words
from .word import Word
from .word_list import WordList

class WordInfo:
    """ Helper class to hold info regarding the Word Form """
    formModel = Word
    listModel = WordList
    masteryFieldName = 'word_id'
    learnedField = 'learnedWords'
    learnedTable = learned_words