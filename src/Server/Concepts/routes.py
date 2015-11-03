from .Controllers import GetConceptLists, GetLearnedConcepts
from Server.helpers import FormEndpoint

from kao_flask import Routes, Endpoint

routes = Routes(FormEndpoint('/api/languages/<int:languageId>/{form}', get=GetLearnedConcepts),
                FormEndpoint('/api/languages/<int:languageId>/{formList}', get=GetConceptLists))