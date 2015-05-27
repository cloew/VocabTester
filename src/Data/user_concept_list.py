from kao_decorators import proxy_for

@proxy_for('conceptList', ['id', 'name'])
class UserConceptList:
    """ Helpful wrapper to perform interactions with a concept list as a particualr user """
    
    def __init__(self, conceptList, user, foreignLanguage):
        """ Initialize the User Concept List with the list, user and requested foreign language """
        self.user = user
        self.foreignLanguage = foreignLanguage
        self.conceptList = conceptList
        
    @property
    def concepts(self):
        """ Return the concepts for the specified languages """
        return self.conceptList.getConceptPairs(self.nativeLanguage, self.foreignLanguage)
        
    @property
    def averageMastery(self):
        """ Return the average mastery of this concept list for the user """
        masteries = [concept.foreign.getMastery(self.user).rating for concept in self.concepts]
        return round(sum(masteries, 0.0) / len(masteries), 1)
        
    @property
    def nativeLanguage(self):
        """ Return the user's native language """
        return self.user.nativeLanguage