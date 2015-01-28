from Data.concept_manager import ConceptManager
from quiz import Quiz
from sampler import sample_at_most

class RandomQuizFactory:
    """ Represents method to contstruct a Quiz from random learned Words or Symbols """
    MAX_QUESTIONS = 10
    
    def buildQuiz(self, formModel, user):
        """ Build a quiz using the from given and the user provided """
        conceptManager = ConceptManager(formModel)
        
        learnedForms = user.getLearnedFor(formModel)
        sample = sample_at_most(learnedForms, self.MAX_QUESTIONS)
        conceptIds = [form.concept_id for form in sample]
        pairs = conceptManager.getConceptPairs(conceptIds, user)
        
        return Quiz("Random List", pairs)
        
RandomQuizFactory = RandomQuizFactory()