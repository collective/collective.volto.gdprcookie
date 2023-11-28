# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.restapi.testing import PloneRestApiDXLayer
from plone.testing import z2


import collective.volto.gdprcookie
import plone.restapi


class VoltoGDPRCookieLayer(PloneSandboxLayer):
    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.volto.gdprcookie)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.volto.gdprcookie:default")


VOLTO_GDPR_COOKIE_FIXTURE = VoltoGDPRCookieLayer()


VOLTO_GDPR_COOKIE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(VOLTO_GDPR_COOKIE_FIXTURE,),
    name="VoltoGDPRCookieLayer:IntegrationTesting",
)


VOLTO_GDPR_COOKIE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(VOLTO_GDPR_COOKIE_FIXTURE,),
    name="VoltoGDPRCookieLayer:FunctionalTesting",
)


VOLTO_GDPR_COOKIE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        VOLTO_GDPR_COOKIE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="VoltoGDPRCookieLayer:AcceptanceTesting",
)


class VoltoGDPRCookieRestApiLayer(PloneRestApiDXLayer):
    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        super(VoltoGDPRCookieRestApiLayer, self).setUpZope(app, configurationContext)

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.volto.gdprcookie)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.volto.gdprcookie:default")


VOLTO_GDPR_COOKIE_API_FIXTURE = VoltoGDPRCookieRestApiLayer()
VOLTO_GDPR_COOKIE_API_INTEGRATION_TESTING = IntegrationTesting(
    bases=(VOLTO_GDPR_COOKIE_API_FIXTURE,),
    name="VoltoGDPRCookieRestApiLayer:Integration",
)

VOLTO_GDPR_COOKIE_API_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(VOLTO_GDPR_COOKIE_API_FIXTURE, z2.ZSERVER_FIXTURE),
    name="VoltoGDPRCookieRestApiLayer:Functional",
)
