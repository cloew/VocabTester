from Data.concept import Concept
from Data.concept_list import ConceptList
from Data.language import Language
from Data.symbol import Symbol
from Data.word import Word

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

def CreateSymbols(symbols, conceptMap, language):
    """ Create the symbols """
    symbols = [Symbol(concept=conceptMap[symbol.conceptId], text=symbol.text, language=language) for symbol in symbols]
    [server.db.session.add(symbol) for symbol in symbols]
    server.db.session.commit()

def CreateWords(words, conceptMap, language):
    """ Create the words """
    words = [Word(concept=conceptMap[word.conceptId], text=word.text, language=language) for word in words]
    [server.db.session.add(word) for word in words]
    server.db.session.commit()
    
def ImportEggs(filename, listName):
    """ Import the words and/or symbols from the given file """
    eggs = LoadEggs(filename)
    
    languageMap = CreateLanguages([egg.language for egg in eggs])
    conceptMap = CreateConcepts(eggs[0].words)
    conceptMap.update(CreateConcepts(eggs[0].symbols))
    
    english = Language.query.filter_by(name="English").first()
    japanese = Language.query.filter_by(name="Japanese").first()
    
    for egg in eggs:
        CreateSymbols(egg.symbols, conceptMap, languageMap[egg.language])
        
    for egg in eggs:
        CreateWords(egg.words, conceptMap, languageMap[egg.language])
        
        
    conceptList = ConceptList(name=listName, concepts=conceptMap.values(), isWords=any([len(egg.words) > 0 for egg in eggs]))
    server.db.session.add(conceptList)
    server.db.session.commit()

def main(args):
    """ Run the main file """
    with server.app.app_context():
        ImportEggs(args[0], args[1])

if __name__ == "__main__":
    main(sys.argv[1:])