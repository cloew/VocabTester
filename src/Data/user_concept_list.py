from kao_decorators import proxy_for

@proxy_for('conceptList', ['id', 'name'])
class UserConceptList:
    """ Helpful wrapper to perform interactions with a concept list as a particular user """
    
    def __init__(self, conceptList, user, conceptManager):
        """ Initialize the User Concept List with the List, User and Concept Manager """
        self.user = user
        self.conceptList = conceptList
        self.conceptManager = conceptManager
        
    @property
    def concepts(self):
        """ Return the concept pairs for the languages in the Concept Manager """
        return self.conceptList.getConceptPairs(self.conceptManager)
        
    @property
    def averageMastery(self):
        """ Return the average Mastery of this Concept List for the User """
        masteries = [concept.foreign.getMastery(self.user).rating for concept in self.concepts]
        return round(sum(masteries, 0.0) / len(masteries), 1)