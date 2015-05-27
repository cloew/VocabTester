from Data.concept_list import ConceptList
from Server import server

class ConceptListLoader:
    """ Class to load a concept list into the database """
    
    def __init__(self, name, eggs, concepts):
        """ Initialize the Concept List """
        self.name = name
        self.concepts = concepts
        self.eggs = eggs
        
    def load(self):
        """ Load the Concept List into the database """
        conceptList = ConceptList(name=self.name, concepts=self.concepts.values(), isWords=any([len(egg.words) > 0 for egg in self.eggs]))
        server.db.session.add(conceptList)
        server.db.session.commit()