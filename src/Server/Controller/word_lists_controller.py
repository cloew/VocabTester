from Server.Data.word_list_wrapper import WordListWrapper

from Data.word_list import WordList
import Data.concept_manager as cm

from auth_json_controller import AuthJSONController

class WordListsController(AuthJSONController):
    """ Controller to return the word lists """
    
    def performWithJSON(self, user=None):
        """ Convert the existing Word Lists to JSON """
        wordLists = WordList.query.all()
        return {"words":[WordListWrapper(wordList).toJSON(cm) for wordList in wordLists]}