from decorators import lazy_property

def query_via(model):
    def addQuery(cls):
        cls.query = QueryProxy(cls, model=model)
        return cls
    return addQuery
    
def new_proxy(fn):
    def wrapQuery(self, *args, **kwargs):
        return QueryProxy(self.clsToReturn, query=fn(self, *args, **kwargs))
    return wrapQuery

class QueryProxy:
    def __init__(self, clsToReturn, model=None, query=None):
        """ Initialize the Query Proxy """
        self.clsToReturn = clsToReturn
        self.queryModel = model
        if query is not None:
            self.query = query
        
    @lazy_property
    def query(self):
        """ Return the user's native language """
        return self.queryModel.query
              
    def first(self):
        """ Return the first query result """
        return self.clsToReturn(self.query.first())
        
    def all(self):
        """ Return all the query results """
        return [self.clsToReturn(entry) for entry in self.query.all()]
        
    @new_proxy
    def filter_by(self, *args, **kwargs):
        """ Return the new filtered query """
        return self.query.filter_by(*args, **kwargs)