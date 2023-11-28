# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel
from collective.volto.gdprcookie.interfaces import IGDPRCookieSettings
from collective.volto.gdprcookie import _


class GDPRCookieForm(controlpanel.RegistryEditForm):
    schema = IGDPRCookieSettings
    label = _("gdpr_cookie_settings_label", default="GDPR Cookie Settings")


class GDPRCookieControlPanel(controlpanel.ControlPanelFormWrapper):
    form = GDPRCookieForm
