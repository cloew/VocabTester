from .import_cmd import ImportCmd

from Data import StalenessPeriod

from kao_command.args import FlagArg
import glob
import os

EGG_DIR = os.path.join(os.path.dirname(__file__), 'resources')

class Seed:
    """ Command to seed the database with all available resource files """
    description = "Seed the database with all available resource files"
    args = [FlagArg('-n', '--no-staleness',  action='store_true', help="Flag to NOT seed Staleness Periods as well")]
    
    def run(self, *, no_staleness=False):
        """ Create the new log entry """
        if not no_staleness:
            self.addStalenessPeriods()
            
        importer = ImportCmd()
        for filename in glob.glob(os.path.join(EGG_DIR, '*.json')):
            importer.run(filename, listName=self.getListName(filename))
    
    def addStalenessPeriods(self):
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

    def getListName(self, filename):
        """ Return the list name for the given file """
        fullPath = os.path.abspath(filename)
        basename = os.path.basename(fullPath)
        filenameWithoutExtension = os.path.splitext(basename)[0]
        pieces = filenameWithoutExtension.split("_")
        
        capitalizedPieces = [piece.capitalize() for piece in pieces]
        return " ".join(capitalizedPieces)