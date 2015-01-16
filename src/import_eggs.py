from Data.concept import Concept
from Data.language import Language
from Data.word import Word
from Data.concept_list import ConceptList

from Server import server

from leggs.egg_loader import LoadEggs
import sys

def CreateLanguages(languageNames):
    """ Create the languages """
    languageMap = {}
    
    for name in languageNames:
        language = Language.query.filter_by(name=name).first()
        if language is None:
            language = Language(name=name)
            server.db.session.add(language)
        languageMap[name] = language
    server.db.session.commit()
    
    return languageMap

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
    
def ImportWords(filename, wordListName):
    """ Import the words from the given file """
    eggs = LoadEggs(filename)
    
    languageMap = CreateLanguages([egg.language for egg in eggs])
    conceptMap = CreateConcepts(eggs[0].words)
    
    english = Language.query.filter_by(name="English").first()
    japanese = Language.query.filter_by(name="Japanese").first()
    
    for egg in eggs:
        CreateWords(egg.words, conceptMap, languageMap[egg.language])
        
    wordList = ConceptList(name=wordListName, concepts=conceptMap.values(), isWords=True)
    server.db.session.add(wordList)
    server.db.session.commit()

def main(args):
    """ Run the main file """
    with server.app.app_context():
        ImportWords(args[0], args[1])

if __name__ == "__main__":
    main(sys.argv[1:])