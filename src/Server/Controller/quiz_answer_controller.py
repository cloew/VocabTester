from Data.mastery import Mastery
from Server.helpers.json_factory import toJson

from auth_json_controller import AuthJSONController

class QuizAnswerController(AuthJSONController):
    """ Controller to create an answer for the quiz """
    
    def performWithJSON(self, masteryId, json=None, user=None):
        """ Create an answer for the mastery """
        mastery = Mastery.query.filter_by(id=masteryId).first()
        mastery.addAnswer(json['correct'])
        return toJson(mastery.word, user=user)