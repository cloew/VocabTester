from Server import server

from import_eggs import ImportEggs

from Data.staleness_period import StalenessPeriod

import glob
import os

EGG_DIR = os.path.join(os.path.dirname(__file__), 'resources/eggs')

def AddStalenessPeriods():
    """ Add the staleness periods """
    previousPeriod = None
    for days in [180, 90, 30, 14, 7]:
        if previousPeriod is not None:
            period = StalenessPeriod(days=days, next=previousPeriod)
        else:
            period = StalenessPeriod(days=days)
        previousPeriod = period
        server.db.session.add(period)
    period = StalenessPeriod(days=3, next=previousPeriod, first=True)
    server.db.session.add(period)
    server.db.session.commit()

def GetListName(filename):
    """ Return the list name for the given file """
    fullPath = os.path.abspath(filename)
    basename = os.path.basename(fullPath)
    filenameWithoutExtension = os.path.splitext(basename)[0]
    pieces = filenameWithoutExtension.split("_")
    
    capitalizedPieces = [piece.capitalize() for piece in pieces]
    return " ".join(capitalizedPieces)

def main():
    with server.app.app_context():
        AddStalenessPeriods()
        for filename in glob.glob(os.path.join(EGG_DIR, '*.json')):
            ImportEggs(filename, listName=GetListName(filename))
            
if __name__ == "__main__":
    main()