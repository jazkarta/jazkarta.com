# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from jazkarta.policy.testing import JAZKARTA_POLICY_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that jazkarta.policy is properly installed."""

    layer = JAZKARTA_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if jazkarta.policy is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('jazkarta.policy'))

    def test_uninstall(self):
        """Test if jazkarta.policy is cleanly uninstalled."""
        self.installer.uninstallProducts(['jazkarta.policy'])
        self.assertFalse(self.installer.isProductInstalled('jazkarta.policy'))
