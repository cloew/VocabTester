
def lazy_property(fn):
    varName = "__{0}".format(fn.__name__)
    def lazyLoad(self):
        if not hasattr(self, varName):
            setattr(self, varName, fn(self))
        return getattr(self, varName)
    return property(lazyLoad)
    
    
def proxy_for(fieldName, attrs):
    def addProxyData(cls):
        def add_property(cls, attr):
            def setter(self, v):
                setattr(getattr(self, fieldName), attr, v)
            def getter(self):
                return getattr(getattr(self, fieldName), attr)
            setattr(cls, attr, property(getter, setter))
            
        for attr in attrs:
            add_property(cls, attr)
        return cls
    return addProxyData