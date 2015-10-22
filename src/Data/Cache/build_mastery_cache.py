from .mastery_cache import MasteryCache

class BuildMasteryCache:
    """ Methods to build a Mastery Cache """
    ViaPairs = lambda pairs, formInfo, user: BuildMasteryCache.ViaForms([pair.foreign for pair in pairs], formInfo, user)
    ViaForms = lambda forms, formInfo, user: MasteryCache(forms, formInfo, user)