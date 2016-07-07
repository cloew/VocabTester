from .ambiguity_group_data import AmbiguityGroupData
from .ambiguity_symbol_data import AmbiguitySymbolData

from kao_factory import DataBoundFactory, Factory, FieldArg
from kao_factory.Source.json_source import JsonSource

AmbiguitySymbolFactory = Factory(AmbiguitySymbolData, FieldArg("text"), FieldArg("clarification"))
AmbiguityGroupFactory = Factory(AmbiguityGroupData, FieldArg("language"), symbols=AmbiguitySymbolFactory.LoadAllArg("symbols"))

def LoadAmbiguityGroups(filename, encoding="utf8"):
    """ Loads the Ambiguity Groups from the file and returns them """
    return DataBoundFactory(AmbiguityGroupFactory, JsonSource(filename, encoding=encoding)).loadAll()