from .behavior import IContentPriority
from plone.indexer import indexer


@indexer(IContentPriority)
def prioritization_start(obj):
    ob = IContentPriority(obj, None)
    if ob is None:
        return None
    return ob.prioritization_start


@indexer(IContentPriority)
def prioritization_end(obj):
    ob = IContentPriority(obj, None)
    if ob is None:
        return None
    return ob.prioritization_end


@indexer(IContentPriority)
def prioritization_level(obj):
    ob = IContentPriority(obj, None)
    if ob is None:
        return None
    return ob.prioritization_level
