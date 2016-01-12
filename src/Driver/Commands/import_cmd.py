from Import.eggs_loader import EggsLoader
from Import.concept_list_loader import ConceptListLoader

from kao_command.args import Arg, FlagArg
from leggs.egg_loader import LoadEggs

class ImportCmd:
    """ Command to import a file and create the necessary Words/Symbols """
    description = "Import a file to seed the database"
    args = [Arg('filename', action='store', help="The file to load"),
            FlagArg('-l', '--listname',  action='store', help="Name of the Concept List to create from the given elements")]
    
    def run(self, *, filename, listname):
        """ Create the new log entry """
        eggs = LoadEggs(filename)
        loader = EggsLoader(eggs)
        loader.load()
        
        if listname is not None:
            ConceptListLoader(listname, eggs, loader.concepts).load()