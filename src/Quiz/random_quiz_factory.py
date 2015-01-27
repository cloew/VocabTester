from Data.concept_manager import ConceptManager
from quiz import Quiz
import random

class RandomQuizFactory:
    """ Represents method to contstruct a Quiz from random learned Words or Symbols """
    MAX_QUESTIONS = 10
    
    def buildQuiz(self, formModel, user):
        """ Build a quiz using the from given and the user provided """
        conceptManager = ConceptManager(formModel)
        
        learnedForms = user.getLearnedFor(formModel)
        sample = random.sample(learnedForms, self.numberOfQuestions(learnedForms))
        conceptIds = [form.concept_id for form in sample]
        pairs = conceptManager.getConceptPairs(conceptIds, user)
        
        return Quiz("Random List", pairs)
        
    def numberOfQuestions(self, learnedForms):
        """ Returns the number of questions allowed for this quiz """
        return min(len(learnedForms), self.MAX_QUESTIONS)
        
RandomQuizFactory = RandomQuizFactory()