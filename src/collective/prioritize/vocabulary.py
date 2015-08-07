from collective.prioritize import _
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import provider


@provider(IVocabularyFactory)
def PrioritizationLevelsVocabulary(context):
    prioritization_levels = [
        ('1', _('high', default=u'High')),
        ('2', _('medium', default=u'Medium')),
        ('3', _('normal', default=u'Normal')),
    ]
    terms = [SimpleTerm(term, term, title=label)
             for term, label in prioritization_levels]
    return SimpleVocabulary(terms)
