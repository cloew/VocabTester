from Server.Question.question_wrapper import QuestionWrapper

class QuizzerWrapper:
    """ Converts a Quizzer to JSON """
    
    def __init__(self, quizzer):
        """ Initialize the quizzer wrapper """
        self.quizzer = quizzer
        
    def toJSON(self):
        """ Convert the word list to JSON """
        return {"name":self.quizzer.quiz.wordList.name,
                "question":QuestionWrapper(self.quizzer.currentQuestion).toJSON(),
                "numberOfQuestions":len(self.quizzer.quiz.questions),
                "currentQuestion":self.quizzer.currentQuestionIndex+1}