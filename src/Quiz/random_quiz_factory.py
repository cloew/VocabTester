from Data.concept_manager import ConceptManager
from quiz import Quiz
from sampler import sample_at_most

class RandomQuizFactory:
    """ Represents method to contstruct a Quiz from random learned Words or Symbols """
    MAX_QUESTIONS = 10
    RATING_RATIOS = [(0, .3),
                     (1, .2),
                     (2, .2),
                     (3, .1),
                     (4, .1),
                     (5, .1)]
    
    def buildQuiz(self, formModel, user):
        """ Build a quiz using the from given and the user provided """
        conceptManager = ConceptManager(formModel)
        
        learnedForms = user.getLearnedFor(formModel)
        formsByRating = self.organizeByMastery(learnedForms, user)
        sample = self.getSampleForQuiz(formsByRating)
        conceptIds = [form.concept_id for form in sample]
        pairs = conceptManager.getConceptPairs(conceptIds, user)
        
        return Quiz("Random List", pairs, user)
        
    def organizeByMastery(self, learnedForms, user):
        """ Return the learned forms organized by their mastery rating """
        forms = {}
        for form in learnedForms:
            rating = form.getMastery(user).rating
            if rating not in forms:
                forms[rating] = [form]
            else:
                forms[rating].append(form)
        return forms
        
    def getSampleForQuiz(self, formsByRating):
        """ Return a sample with forms weighted via their mastery rating """
        numberPerRating = self.getNumberPerRating(formsByRating)
        sample = []
        
        for rating in numberPerRating:
            if rating in formsByRating:
                entries = sample_at_most(formsByRating[rating], numberPerRating[rating])
                sample += entries
        return sample
        
    def getNumberPerRating(self, formsByRating):
        """ Return the number of entries for each rating that should be used """
        numberPerRating = {}
        hasMoreForms = {}
        for rating, weight in self.RATING_RATIOS:
            hasMoreForms[rating] = rating in formsByRating
            if hasMoreForms[rating]:
                numberPerRating[rating] = min(len(formsByRating[rating]), int(weight*self.MAX_QUESTIONS))
            else:
                numberPerRating[rating] = 0
            
        while sum(numberPerRating.values()) < self.MAX_QUESTIONS and any(hasMoreForms.values()):
            for rating, weight in self.RATING_RATIOS:
                if hasMoreForms[rating]:
                    amountLeftover = self.MAX_QUESTIONS - sum(numberPerRating.values())
                    numberThatCanBeAdded = len(formsByRating[rating]) - numberPerRating[rating]
                    
                    numberPerRating[rating] += min(numberThatCanBeAdded, amountLeftover)
                    hasMoreForms[rating] = not (numberPerRating[rating] == len(formsByRating[rating]))
        
        return numberPerRating
        
RandomQuizFactory = RandomQuizFactory()