
class Quizzer:
    """ Represents a running quiz """
    
    def __init__(self, quiz):
        """ Initialize the quizzer with the quiz """
        self.quiz = quiz
        self.currentQuestion = self.quiz.start()
        self.questionResults = []
        self.completed = False
        
    def answer(self, answerIndex):
        """ Answer the current question with the given answer index """
        if self.completed:
            return
        
        results = self.currentQuestion.answer(answerIndex)
        self.questionResults.append(results)
        try:
            self.currentQuestion = self.quiz.nextQuestion()
        except StopIteration:
            self.completed = True
       
    @property
    def latestResults(self):
        """ Return the latest question results """
        return self.questionResults[-1]
       
    @property
    def currentQuestionIndex(self):
        """ Return the current question index """
        return len(self.questionResults)