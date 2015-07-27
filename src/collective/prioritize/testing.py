# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.prioritize


class CollectivePrioritizeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.prioritize)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.prioritize:default')


COLLECTIVE_PRIORITIZE_FIXTURE = CollectivePrioritizeLayer()


COLLECTIVE_PRIORITIZE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_PRIORITIZE_FIXTURE,),
    name='CollectivePrioritizeLayer:IntegrationTesting'
)


COLLECTIVE_PRIORITIZE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_PRIORITIZE_FIXTURE,),
    name='CollectivePrioritizeLayer:FunctionalTesting'
)


COLLECTIVE_PRIORITIZE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_PRIORITIZE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectivePrioritizeLayer:AcceptanceTesting'
)
