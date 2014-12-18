from Data.Question.question import Question
import random

class Quiz:
    """ Represents a quiz for a list of words """
    
    def __init__(self, concepts, nativeLanguage, testLanguage, conceptManager):
        """ Initialize the Quizzer with the concepts to test and the native and test languages """
        self.nativeLanguage = nativeLanguage
        self.testLanguage = testLanguage
        
        wordsInNativeLanguage = conceptManager.findConceptMatches(concepts, nativeLanguage)
        translations = set(conceptManager.findConceptMatches(concepts, testLanguage))
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