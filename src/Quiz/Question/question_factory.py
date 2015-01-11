from question import Question
import random

class QuestionFactory:
    """ Constructs Questions """
    
    def buildQuestions(self, wordList, conceptManager):
        """ Build the questions for use in the quiz """
        wordsInNativeLanguage = wordList.getNativeWords(conceptManager)
        translations = set(wordList.getTranslatedWords(conceptManager))
        random.shuffle(wordsInNativeLanguage)
        
        questions = []
        for word in wordsInNativeLanguage:
            translation = conceptManager.findTranslation(word, wordList.testLanguage)
            translations.remove(translation)
            questions.append(Question(word, translation, translations))
            translations.add(translation)
            
        return questions
        
QuestionFactory = QuestionFactory()