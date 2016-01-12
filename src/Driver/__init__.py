from .Commands import commands
from kao_command import Driver

def VocabImporter(scriptName):
    return Driver(scriptName, commands)