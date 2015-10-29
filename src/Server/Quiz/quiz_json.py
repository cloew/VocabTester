from Data import Word
from Quiz import Quiz, OptionsQuestion, ForeignPromptQuestion, QuestionTypes, GradeResult
from kao_json import JsonFactory, AsObj, ViaAttr

def answerUrl(context):
    """ Returns the mastery rating for the word and user """
    question = context.obj
    masteryCache = context.args.masteryCache
    return "/api/mastery/{0}/answer".format(masteryCache[question.subject.foreign.id].id)
    
def IsWordsQuiz(context):
    """ Returns if the quiz is for words """
    quiz = context.obj
    return len(quiz.questions) == 0 or quiz.questions[0].subject.foreign.__class__ is Word

QuizJson = {GradeResult:AsObj(correct=ViaAttr(), imperfect=ViaAttr()),
            OptionsQuestion:AsObj(subject=ViaAttr(), queryWord=ViaAttr(), options=ViaAttr(), answerIndex=ViaAttr(), questionType=lambda ctx: QuestionTypes.Options, 
                                  answerUrl=answerUrl),
            ForeignPromptQuestion:AsObj(subject=ViaAttr(), prompt=ViaAttr(), answer=ViaAttr(), displayAnswer=ViaAttr(), questionType=lambda ctx: QuestionTypes.Prompt,
                                  answerUrl=answerUrl),
            Quiz:AsObj(name=ViaAttr(), questions=ViaAttr(), isWords=IsWordsQuiz),
           }