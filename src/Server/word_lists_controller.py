from word_list_wrapper import WordListWrapper

from Data.concept_manager import ConceptManager
from Data.word_list import WordList

from kao_flask.controllers.json_controller import JSONController

class WordListsController(JSONController):
    """ Controller to return the word lists """
    cm = ConceptManager(["resources/days_of_week_english.json", "resources/days_of_week_japanese.json"])
    
    def performWithJSON(self):
        """ Convert the existing Word Lists to JSON """
        wordList = WordList("Days of the Week", range(1,8), "English", "Japanese")
        return {"words":[WordListWrapper(wordList).toJSON(self.cm)]}