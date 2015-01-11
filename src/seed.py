from Server import server

from import_eggs import ImportWords

import glob
import os

EGG_DIR = os.path.join(os.path.dirname(__file__), 'resources/eggs')

def GetWordListName(filename):
    """ Return the word list name for the given file """
    fullPath = os.path.abspath(filename)
    basename = os.path.basename(fullPath)
    filenameWithoutExtension = os.path.splitext(basename)[0]
    pieces = filenameWithoutExtension.split("_")
    
    capitalizedPieces = [piece.capitalize() for piece in pieces]
    return " ".join(capitalizedPieces)

def main():
    with server.app.app_context():
        for filename in glob.glob(os.path.join(EGG_DIR, '*.json')):
            ImportWords(filename, GetWordListName(filename))
            
if __name__ == "__main__":
    main()