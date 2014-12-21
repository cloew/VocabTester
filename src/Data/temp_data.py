from Data.concept_manager import ConceptManager
from Data.word_list import WordList

from Quiz.quiz import Quiz
from Quiz.quizzer import Quizzer

cm = ConceptManager(["resources/days_of_week_english.json", "resources/days_of_week_japanese.json"])
wordList = WordList("Days of the Week", range(1,8), "English", "Japanese")
quizzer = None

def BuildQuiz():
    """ Build the Quiz """
    global quizzer, wordList, cm
    quizzer = Quizzer(Quiz(wordList, cm))
    return quizzer
    
def GetQuiz():
    """ Return the current quiz """
    global quizzer
    return quizzer