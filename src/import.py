from Data.concept import Concept
from Data.language import Language
from Data.word import Word
from Data.word_list import WordList

from Server import server

from leggs.egg_loader import LoadEggs
import sys

def CreateLanguages(languageNames):
    """ Create the languages """
    languages = [Language(name=name) for name in languageNames]
    [server.db.session.add(language) for language in languages]
    server.db.session.commit()
    return {name:language for name, language in zip(languageNames, languages)}

def CreateConcepts(words):
    """ Create the concepts """
    concepts = [Concept() for word in words]
    [server.db.session.add(concept) for concept in concepts]
    server.db.session.commit()
    return {word.conceptId:concept for word, concept in zip(words, concepts)}

def CreateWords(words, conceptMap, language):
    """ Create the concepts """
    words = [Word(concept=conceptMap[word.conceptId], text=word.text, language=language) for word in words]
    [server.db.session.add(word) for word in words]
    server.db.session.commit()

def main(args):
    """ Run the main file """
    with server.app.app_context():
        eggs = LoadEggs(args[0])
        
        languageMap = CreateLanguages([egg.language for egg in eggs])
        conceptMap = CreateConcepts(eggs[0].words)
        
        for egg in eggs:
            CreateWords(egg.words, conceptMap, languageMap[egg.language])
        
        # for table in [WordList, Word, Language, Concept]:
            # records = table.query.all()
            # [server.db.session.delete(record) for record in records]
        # server.db.session.commit()

if __name__ == "__main__":
    main(sys.argv[1:])