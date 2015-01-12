from Server.Data.word_list_wrapper import WordListWrapper

from Data.word_list import WordList
import Data.concept_manager as cm

from kao_flask.controllers.json_controller import JSONController

class WordListsController(JSONController):
    """ Controller to return the word lists """
    
    def performWithJSON(self):
        """ Convert the existing Word Lists to JSON """
        wordLists = WordList.query.all()
        return {"words":[WordListWrapper(wordList).toJSON(cm) for wordList in wordLists]}