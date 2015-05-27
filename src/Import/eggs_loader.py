from .egg_wrapper import EggWrapper
from .concept_dictionary import ConceptDictionary

from Server import server

from leggs.egg_loader import LoadEggs

class EggsLoader:
    """ Class to load Language Eggs """
    
    def __init__(self, eggs):
        """ Initialize the eggs loader with the file to load eggs from """
        self.eggs = [EggWrapper(egg) for egg in eggs]
        self.concepts = ConceptDictionary(self.eggs)
        
    def load(self):
        """ Load the eggs into the database """
        for egg in self.eggs:
            egg.load(self.concepts)
        server.db.session.commit()