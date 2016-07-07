from Import import AmbiguityLoader, LoadAmbiguityGroups

from kao_command.args import Arg

class ImportAmbiguityCmd:
    """ Command to import an Ambiguity Group file and create the proper Ambiguity Groups """
    description = "Import a file to seed the Ambiguity Groups"
    args = [Arg('filename', action='store', help="The file to load")]
    
    def run(self, *, filename):
        """ Create the new log entry """
        groups = LoadAmbiguityGroups(filename)
        loader = AmbiguityLoader(groups)
        
        loader.load()