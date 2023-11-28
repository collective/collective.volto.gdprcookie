# -*- coding: utf-8 -*-
from collective.volto.gdprcookie.interfaces import IGDPRCookieSettings
from plone.restapi.deserializer import json_body
from plone.restapi.deserializer.controlpanels import (
    ControlpanelDeserializeFromJson,
)
from plone.restapi.deserializer.blocks import path2uid
from plone.restapi.interfaces import IDeserializeFromJson
from Products.CMFPlone.utils import safe_unicode
from zExceptions import BadRequest
from zope.component import adapter
from zope.interface import implementer

import json
import lxml


@implementer(IDeserializeFromJson)
@adapter(IGDPRCookieSettings)
class GDPRCookieSettingsDeserializeFromJson(ControlpanelDeserializeFromJson):
    def __call__(self):
        """
        Convert json data into a string
        """
        req = json_body(self.controlpanel.request)
        proxy = self.registry.forInterface(self.schema, prefix=self.schema_prefix)
        errors = []

        settings = req.get("settings", {})
        if not settings:
            errors.append(
                {
                    "message": "Missing data",
                    "field": "settings",
                }
            )
            raise BadRequest(errors)
        try:
            setattr(proxy, "settings", json.dumps(settings))
        except ValueError as e:
            errors.append(
                {
                    "message": str(e),
                    "field": "settings",
                    "error": e,
                }
            )

        if errors:
            raise BadRequest(errors)
