from collective.prioritize import _
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import provider


@provider(IVocabularyFactory)
def PrioritizationLevelsVocabulary(context):
    prioritization_levels = [
        ('high', _('high', default=u'High')),
        ('medium', _('medium', default=u'Medium')),
        ('normal', _('normal', default=u'Normal')),
    ]
    terms = [SimpleTerm(term, term, title=label)
             for term, label in prioritization_levels]
    return SimpleVocabulary(terms)
