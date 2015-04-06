# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import jazkarta.plonetheme


class JazkartaPlonethemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            jazkarta.plonetheme,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'jazkarta.plonetheme:default')


JAZKARTA_PLONETHEME_FIXTURE = JazkartaPlonethemeLayer()


JAZKARTA_PLONETHEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(JAZKARTA_PLONETHEME_FIXTURE,),
    name='JazkartaPlonethemeLayer:IntegrationTesting'
)


JAZKARTA_PLONETHEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(JAZKARTA_PLONETHEME_FIXTURE,),
    name='JazkartaPlonethemeLayer:FunctionalTesting'
)


JAZKARTA_PLONETHEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        JAZKARTA_PLONETHEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='JazkartaPlonethemeLayer:AcceptanceTesting'
)
