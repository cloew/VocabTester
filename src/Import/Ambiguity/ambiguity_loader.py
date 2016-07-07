from Server import server

class AmbiguityLoader:
    """ Loads Ambiguity Groups and assigns Symbols to them """
    
    def __init__(self, groups):
        """ Initialize with the Groups to load """
        self.groups = groups
        
    def load(self):
        """ Load the Group Data """
        for group in self.groups:
            group.assign()
        server.db.session.commit()