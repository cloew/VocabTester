from Server.Question.question_wrapper import QuestionWrapper

class QuizWrapper:
    """ Converts a Quiz to JSON """
    
    def __init__(self, quiz):
        """ Initialize the quiz wrapper """
        self.quiz = quiz
        
    def toJSON(self):
        """ Convert the word list to JSON """
        return {"name":self.quiz.wordList.name,
                "questions":[QuestionWrapper(question).toJSON() for question in self.quiz.questions]}