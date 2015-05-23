from Import.eggs_loader import EggsLoader
from Import.concept_list_loader import ConceptListLoader

from Server import server

from leggs.egg_loader import LoadEggs
import sys
    
def ImportEggs(filename, listName=None):
    """ Import the words and/or symbols from the given file """
    eggs = LoadEggs(filename)
    loader = EggsLoader(eggs)
    loader.load()
    
    if listName is not None:
        ConceptListLoader(listName, eggs, loader.concepts).load()

def main(args):
    """ Run the main file """
    with server.app.app_context():
        ImportEggs(args[0], listName=args[1] if len(args) > 1 else None)

if __name__ == "__main__":
    main(sys.argv[1:])