from Data.concept_manager import ConceptManager
from Data.word_list import WordList

from Quiz.quiz import Quiz
from Quiz.quizzer import Quizzer

cm = ConceptManager(["resources/days_of_week_english.json", "resources/days_of_week_japanese.json"])
wordList = None
quizzer = None

def GetWordList():
    global wordList
    if wordList is None:
        wordList = WordList.query.first()
    return wordList

def BuildQuiz():
    """ Build the Quiz """
    global quizzer, cm
    wordList = GetWordList()
    quizzer = Quizzer(Quiz(wordList, cm))
    return quizzer
    
def GetQuiz():
    """ Return the current quiz """
    global quizzer
    return quizzer