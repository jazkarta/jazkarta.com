# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from jazkarta.plonetheme.testing import JAZKARTA_PLONETHEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that jazkarta.plonetheme is properly installed."""

    layer = JAZKARTA_PLONETHEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if jazkarta.plonetheme is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('jazkarta.plonetheme'))

    def test_uninstall(self):
        """Test if jazkarta.plonetheme is cleanly uninstalled."""
        self.installer.uninstallProducts(['jazkarta.plonetheme'])
        self.assertFalse(self.installer.isProductInstalled('jazkarta.plonetheme'))

    def test_browserlayer(self):
        """Test that IJazkartaPlonethemeLayer is registered."""
        from jazkarta.plonetheme.interfaces import IJazkartaPlonethemeLayer
        from plone.browserlayer import utils
        self.assertIn(IJazkartaPlonethemeLayer, utils.registered_layers())
