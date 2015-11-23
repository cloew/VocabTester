
class FilteredQuery:
    """ Helper Descriptor to ensure a query is always filtered """
    
    def __init__(self, base, **kwargs):
        """ Initialize with the Base Cls to query with and the filter_by keyword args """
        self.base = base
        self.kwargs = kwargs

    def __get__(self, obj, owner):
        """ Return the proper query """
        superClass = super(self.base, obj) if obj is not None else super(self.base, owner)
        return superClass.query.filter_by(**self.kwargs)