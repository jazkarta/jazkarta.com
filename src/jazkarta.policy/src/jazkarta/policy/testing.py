# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import jazkarta.policy


class JazkartaPolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            jazkarta.policy,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'jazkarta.policy:default')


JAZKARTA_POLICY_FIXTURE = JazkartaPolicyLayer()


JAZKARTA_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(JAZKARTA_POLICY_FIXTURE,),
    name='JazkartaPolicyLayer:IntegrationTesting'
)


JAZKARTA_POLICY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(JAZKARTA_POLICY_FIXTURE,),
    name='JazkartaPolicyLayer:FunctionalTesting'
)


JAZKARTA_POLICY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        JAZKARTA_POLICY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='JazkartaPolicyLayer:AcceptanceTesting'
)
