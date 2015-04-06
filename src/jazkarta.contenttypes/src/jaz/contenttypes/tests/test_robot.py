from  jaz.contenttypes.testing import JAZ_CONTENTTYPES_FUNCTIONAL_TESTING
from plone.testing import layered
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("robot_test.txt"),
                layer=JAZ_CONTENTTYPES_FUNCTIONAL_TESTING)
    ])
    return suite