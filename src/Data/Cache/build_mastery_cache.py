from .mastery_cache import MasteryCache

class BuildMasteryCache:
    """ Methods to build a Mastery Cache """
    ViaPairs = lambda pairs, formCls, user: BuildMasteryCache.ViaForms([pair.foreign for pair in pairs], formCls, user)
    ViaForms = lambda forms, formCls, user: MasteryCache(forms, formCls, user)