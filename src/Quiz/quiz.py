from Quiz.Question.question_factory import QuestionFactory

class Quiz:
    """ Represents a quiz for a list of words """
    
    def __init__(self, name, pairs, user):
        """ Initialize the Quiz with the word list to test """
        self.name = name
        self.pairs = pairs
        self.questions = QuestionFactory.buildQuestions(pairs, user)
            
    def start(self):
        """ Start the Quiz """
        self.nextQuestionCoroutine = self.getNextQuestion()
        return self.nextQuestion()
        
    def nextQuestion(self):
        """ Return the next question """
        return self.nextQuestionCoroutine.next()
            
    def getNextQuestion(self):
        """ Yield the next question """
        for question in self.questions:
            yield question