import Data.concept_manager as cm
from Data.word_list import WordList

from Quiz.quiz import Quiz
from Quiz.quizzer import Quizzer

wordList = None
quizzer = None

def GetWordList():
    global wordList
    if wordList is None:
        wordList = WordList.query.first()
    return wordList

def BuildQuiz():
    """ Build the Quiz """
    global quizzer
    wordList = GetWordList()
    quizzer = Quizzer(Quiz(wordList, cm))
    return quizzer
    
def GetQuiz():
    """ Return the current quiz """
    global quizzer
    return quizzer