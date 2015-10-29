
class ConceptPair:
    """ Represents the forms of a concept in both the user's native and foreign languages """

    def __init__(self, native, foreign):
        """ Initialize the Pair with both the native and foreign forms """
        self.native = native
        self.foreign = foreign
        
    def getMasteryForUser(self, user):
        """ Return the mastery for the foreign form for the user """
        return self.foreign.getMastery(user)