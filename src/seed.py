from Data.concept import Concept
from Data.language import Language
from Data.word import Word
from Data.word_list import WordList

from Server import server

NUM_DAYS = 7

def main():
    with server.app.app_context():
        concepts = Concept.query.all()
        english = Language.query.filter_by(name="English").first()
        japanese = Language.query.filter_by(name="Japanese").first()
        
        wordList = WordList(name="Days of the Week", concepts=concepts, nativeLanguage=english, testLanguage=japanese)
        server.db.session.add(wordList)
        server.db.session.commit()
        
        for table in [WordList, Word, Language, Concept]:
            records = table.query.all()
            print records

if __name__ == "__main__":
    main()