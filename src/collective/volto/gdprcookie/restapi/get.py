from collective.volto.gdprcookie.interfaces import IGDPRCookieSettings
from plone import api
from plone.restapi.services import Service
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse

import json


@implementer(IPublishTraverse)
class GDPRCookieSettingsGet(Service):
    def get_field_value(self, field):
        """
        Return value from registry
        """
        return (
            api.portal.get_registry_record(field, interface=IGDPRCookieSettings) or None
        )

    def reply(self):
        """
        Return settings
        """
        enabled = self.get_field_value(field="banner_enabled")
        if not enabled:
            return {}
        show_icon = self.get_field_value(field="show_icon")
        technical_cookies_only = self.get_field_value(field="technical_cookies_only")
        settings = self.get_field_value(field="settings")
        if settings:
            settings = json.loads(settings)

        data = {
            "show_icon": show_icon,
        }
        if technical_cookies_only and "profiling" in settings:
            del settings["profiling"]
        data.update(settings)
        return data
