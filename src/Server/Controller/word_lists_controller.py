from Server.decorators import requires_auth
from Server.Data.word_list_wrapper import WordListWrapper

from Data.word_list import WordList
import Data.concept_manager as cm

from kao_flask.controllers.json_controller import JSONController

class WordListsController(JSONController):
    """ Controller to return the word lists """
    
    def __init__(self):
        """ Initialize the JSON Controller with its required decorators """
        JSONController.__init__(self, decorators=[requires_auth])
        
    def performWithJSON(self):
        """ Convert the existing Word Lists to JSON """
        wordLists = WordList.query.all()
        return {"words":[WordListWrapper(wordList).toJSON(cm) for wordList in wordLists]}