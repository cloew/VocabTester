from word_list_wrapper import WordListWrapper

from Data.temp_data import wordList, cm

from kao_flask.controllers.json_controller import JSONController

class WordListsController(JSONController):
    """ Controller to return the word lists """
    
    def performWithJSON(self):
        """ Convert the existing Word Lists to JSON """
        return {"words":[WordListWrapper(wordList).toJSON(cm)]}