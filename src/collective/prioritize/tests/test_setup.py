# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.prioritize.testing import COLLECTIVE_PRIORITIZE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.prioritize is properly installed."""

    layer = COLLECTIVE_PRIORITIZE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.prioritize is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.prioritize'))

    def test_browserlayer(self):
        """Test that ICollectivePrioritizeLayer is registered."""
        from collective.prioritize.interfaces import ICollectivePrioritizeLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectivePrioritizeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_PRIORITIZE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.prioritize'])

    def test_product_uninstalled(self):
        """Test if collective.prioritize is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('collective.prioritize'))

    def test_browserlayer_removed(self):
        """Test that ICollectivePrioritizeLayer is removed."""
        from collective.prioritize.interfaces import ICollectivePrioritizeLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectivePrioritizeLayer, utils.registered_layers())
