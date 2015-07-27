# -*- coding: utf-8 -*-
from collective.prioritize import _
from plone.app.z3cform.widget import DatetimeFieldWidget
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from zope.interface import provider


@provider(IFormFieldProvider)
class IContentPriority(model.Schema):
    """Adds a field for navigation title after the original title.
    """

    model.fieldset(
        'dates',
        label=_(u'label_schema_dates', default=u'Dates'),
        fields=['prioritization_start', 'prioritization_end',
                'prioritization_level'],
    )

    prioritization_start = schema.Datetime(
        title=_(u'label_prioritization_start', u'Prioritization Start Date'),
        description=_(
            u'help_prioritization_start',
            default=u"Start of content prioritization"),
        required=False
    )
    directives.widget('prioritization_start', DatetimeFieldWidget)

    prioritization_end = schema.Datetime(
        title=_(u'label_prioritization_end', u'Prioritization End Date'),
        description=_(
            u'help_prioritization_end',
            default=u"End of content prioritization"),
        required=False
    )
    directives.widget('prioritization_end', DatetimeFieldWidget)

    prioritization_level = schema.Choice(
        title=_(u'label_prioritization_level', default=u'Prioritization Level'),
        vocabulary='collective.prioritize.PrioritizationLevels',
        required=False,
        missing_value='',
    )
    directives.widget('prioritization_level', SelectFieldWidget)


@implementer(IContentPriority)
class ContentPriority(object):
    """
    """

    def __init__(self, context):
        self.context = context

    @property
    def prioritization_start(self):
        return getattr(self.context, '_prioritization_start', None)

    @prioritization_start.setter
    def prioritization_start(self, value):
        self.context._prioritization_start = value

    @property
    def prioritization_end(self):
        return getattr(self.context, '_prioritization_end', None)

    @prioritization_end.setter
    def prioritization_end(self, value):
        self.context._prioritization_end = value

    @property
    def prioritization_level(self):
        return getattr(self.context, '_prioritization_level', None)

    @prioritization_level.setter
    def prioritization_level(self, value):
        self.context._prioritization_level = value
