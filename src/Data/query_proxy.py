from decorators import lazy_property

class QueryProxy:
    def __init__(self, queryModel, clsToReturn):
        """ Initialize the Query Proxy """
        self.queryModel = queryModel
        self.clsToReturn = clsToReturn
        self.__query = None
        
    def __getattr__(self, name):
        if hasattr(self, name):
            return getattr(self, name)
        elif self.query:
              return getattr(self.query, name )
        else:
              raise Exception( 'attribute %s not found' % name )
        
    @lazy_property
    def query(self):
        """ Return the user's native language """
        if self.__query is None:
            self.__query = self.queryModel.query
        return self.__query
              
    def first(self):
        """ Return the first query result """
        return self.clsToReturn(self.query.first())
        
    def all(self):
        """ Return all the query results """
        return [self.clsToReturn(entry) for entry in self.query.all()]