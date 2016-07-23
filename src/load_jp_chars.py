from Data import Language, User, Symbol, SymbolInfo
from Data.Cache import LearnedCache

from Server import server

from kao_flask.ext.sqlalchemy import db
import sys
        
def main(args):
    """ Run the main file """
    with server.app.app_context():
        japanese = Language.query.filter_by(name='Japanese').first()
        user = User.query.filter_by(email=args[0]).first()
        
        symbolText = 'っゃゅょッャュョヴァィゥェォ'
        symbols = Symbol.query.filter(Symbol.text.in_(symbolText)).filter_by(language=japanese).all()
        symbolMap = {symbol.text:symbol for symbol in symbols}
        
        newSymbols = []
        for char in symbolText:
            if char not in symbolMap:
                symbol = Symbol(text=char, language=japanese)
                newSymbols.append(symbol)
                symbols.append(symbol)
        db.session.add_all(newSymbols)
        
        learnedCache = LearnedCache(user, SymbolInfo)
        for symbol in symbols:
            user.tryToLearn(symbol, SymbolInfo, learnedCache)
        db.session.commit()
            
if __name__ == "__main__":
    main(sys.argv[1:])