
def lazy_property(fn):
    varName = "__{0}".format(fn.__name__)
    def lazyLoad(self):
        if not hasattr(self, varName):
            setattr(self, varName, fn(self))
        return getattr(self, varName)
    return property(lazyLoad)