from quiz import Quiz
import random

class RandomQuizFactory:
    """ Represents method to contstruct a Quiz from random learned Words or Symbols """
    MAX_QUESTIONS = 10
    
    def buildQuiz(self, formModel, user):
        """ Build a quiz using the from given and the user provided """
        learnedForms = user.getLearnedFor(formModel)
        sample = random.sample(learnedForms, self.numberOfQuestions(learnedFroms))
        conceptIds = [form.concept_id for form in sample]
        pairs = self.conceptManager.getConceptPairs(conceptIds, user)
        return Quiz("Random List", pairs)
        
    def numberOfQuestions(self, learnedFroms):
        """ Returns the number of questions allowed for this quiz """
        return min(len(learnedForms), self.MAX_QUESTIONS)
        
RandomQuizFactory = RandomQuizFactory()