from Data import Word
from Quiz import Quiz, OptionsQuestion, ForeignPromptQuestion, QuestionTypes, GradeResult
from kao_json import JsonFactory, JsonAttr, FieldAttr, StaticAttr

def answerUrl(question, user):
    """ Returns the mastery rating for the word and user """    
    return "/api/mastery/{0}/answer".format(question.subject.getMasteryForUser(user).id)
    
def IsWordsQuiz(quiz):
    """ Returns if the quiz is for words """    
    return len(quiz.questions) == 0 or quiz.questions[0].subject.foreign.__class__ is Word

QuizJson = [
            (GradeResult, [FieldAttr('correct'), FieldAttr('imperfect')]),
            (OptionsQuestion, [FieldAttr('subject'), FieldAttr('queryWord'), FieldAttr('options'), FieldAttr('answerIndex'), StaticAttr('questionType', QuestionTypes.Options), JsonAttr('answerUrl', answerUrl, args=["user"])]),
            (ForeignPromptQuestion, [FieldAttr('subject'), FieldAttr('prompt'), FieldAttr('answer'), FieldAttr('displayAnswer'), StaticAttr('questionType', QuestionTypes.Prompt), JsonAttr('answerUrl', answerUrl, args=["user"])]),
            (Quiz, [FieldAttr('name'), FieldAttr('questions'), JsonAttr('isWords', IsWordsQuiz)]),
           ]