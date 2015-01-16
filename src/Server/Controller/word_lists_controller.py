from Data.word_list import WordList

from Server.Data.json_factory import toJson
from auth_json_controller import AuthJSONController

class WordListsController(AuthJSONController):
    """ Controller to return the word lists """
    
    def performWithJSON(self, json=None, user=None):
        """ Convert the existing Word Lists to JSON """
        wordLists = WordList.query.all()
        return {"words":toJson(wordLists, user=user)}