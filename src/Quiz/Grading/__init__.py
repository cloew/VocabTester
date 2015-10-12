from .grade_result import GradeResult
from .options_grader import OptionsGrader
from .prompt_grader import PromptGrader
from ..Question import QuestionTypes

Graders = {QuestionTypes.Options: OptionsGrader(),
           QuestionTypes.Prompt: PromptGrader()}