from Data import Word
from Quiz import Quiz, OptionsQuestion, ForeignPromptQuestion, QuestionTypes, GradeResult
from kao_json import JsonFactory, AsObj, ViaAttr, ViaFn

def answerUrl(question, masteryCache):
    """ Returns the mastery rating for the word and user """
    return "/api/mastery/{0}/answer".format(masteryCache[question.subject.foreign.id].id)
    
def IsWordsQuiz(quiz):
    """ Returns if the quiz is for words """
    return len(quiz.questions) == 0 or quiz.questions[0].subject.foreign.__class__ is Word

QuizJson = {GradeResult:AsObj(correct=ViaAttr(), imperfect=ViaAttr()),
            OptionsQuestion:AsObj(subject=ViaAttr(), queryWord=ViaAttr(), options=ViaAttr(), answerIndex=ViaAttr(), questionType=lambda ctx: QuestionTypes.Options, 
                                  answerUrl=ViaFn(answerUrl, requires=['masteryCache'])),
            ForeignPromptQuestion:AsObj(subject=ViaAttr(), prompt=ViaAttr(), answer=ViaAttr(), displayAnswer=ViaAttr(), questionType=lambda ctx: QuestionTypes.Prompt,
                                  answerUrl=ViaFn(answerUrl, requires=['masteryCache'])),
            Quiz:AsObj(name=ViaAttr(), questions=ViaAttr(), isWords=ViaFn(IsWordsQuiz)),
           }