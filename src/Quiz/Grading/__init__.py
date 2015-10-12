from .options_grader import OptionsGrader
from ..Question import QuestionTypes

Graders = {QuestionTypes.Options: OptionsGrader(),
           QuestionTypes.Prompt: OptionsGrader()}