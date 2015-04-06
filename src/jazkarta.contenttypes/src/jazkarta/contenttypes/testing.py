from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class JazcontenttypesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import jazkarta.contenttypes
        xmlconfig.file(
            'configure.zcml',
            jazkarta.contenttypes,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        # z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'jazkarta.contenttypes:default')

JAZ_CONTENTTYPES_FIXTURE = JazcontenttypesLayer()
JAZ_CONTENTTYPES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(JAZ_CONTENTTYPES_FIXTURE,),
    name="JazcontenttypesLayer:Integration"
)
JAZ_CONTENTTYPES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(JAZ_CONTENTTYPES_FIXTURE, z2.ZSERVER_FIXTURE),
    name="JazcontenttypesLayer:Functional"
)
