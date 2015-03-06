from kao_decorators import lazy_property

class OptionsFinder:
    """ Helper class to determine the porper potential options for a question """
    
    def __init__(self, subject, allPairs):
        """ Initialize the option finder with the subject and all the concept pairs for the quiz """
        self.subject = subject
        self.allPairs = allPairs
        
    @lazy_property
    def options(self):
        """ Return the proper options """
        return [option for option in self.allPairs if self.validOption(option)]
        
    def validOption(self, option):
        """ Return if the option is a valid option for the question """
        return all([self.notSubject(option), self.noConflict(option)])
        
    def notSubject(self, option):
        """ Return if the option is not the subject of the question """
        return option is not self.subject
    
    def noConflict(self, option):
        """ Return if the option and subject do not conflict with their native or foreign forms """
        return (not option.native.text == self.subject.native.text) and (not option.foreign.text == self.subject.foreign.text)