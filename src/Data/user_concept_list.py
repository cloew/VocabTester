from kao_decorators import proxy_for

@proxy_for('conceptList', ['id', 'name'])
class UserConceptList:
    """ Helpful wrapper to perform interactions with a concept list as a user """
    
    def __init__(self, conceptList, user):
        """ Initialize the User Concept List with the list and the user """
        self.user = user
        self.conceptList = conceptList
        
    @property
    def concepts(self):
        """ Return the concepts for the user's language """
        return self.conceptList.getConceptPairs(self.user)
        
    @property
    def averageMastery(self):
        """ Return the average mastery of this concept list for the user """
        masteries = [concept.foreign.getMastery(self.user).rating for concept in self.concepts]
        return round(sum(masteries, 0.0) / len(masteries), 1)