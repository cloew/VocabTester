from Quiz.Question.question import Question
import random

class Quiz:
    """ Represents a quiz for a list of words """
    
    def __init__(self, wordList, conceptManager):
        """ Initialize the Quiz with the word list to test """
        self.wordList = wordList
        wordsInNativeLanguage = wordList.getNativeWords(conceptManager)
        translations = set(wordList.getTranslatedWords(conceptManager))
        random.shuffle(wordsInNativeLanguage)
        
        self.questions = []
        for word in wordsInNativeLanguage:
            translation = conceptManager.findTranslation(word, testLanguage)
            translations.remove(translation)
            self.questions.append(Question(word, translation, translations))
            translations.add(translation)
            
    def start(self):
        """ Start the Quiz """
        self.nextQuestionCoroutine = self.getNextQuestion()
        return self.nextQuestion()
        
    def nextQuestion(self):
        """ Return the next question """
        return self.nextQuestionCoroutine.next()
            
    def getNextQuestion(self):
        """ Yield the next question """
        for question in self.questions:
            yield question