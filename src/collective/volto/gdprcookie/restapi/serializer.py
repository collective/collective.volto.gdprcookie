from collective.volto.gdprcookie.interfaces import IGDPRCookieSettings
from plone.restapi.interfaces import ISerializeToJson
from plone.restapi.serializer.controlpanels import ControlpanelSerializeToJson
from zope.component import adapter
from zope.interface import implementer

import json
import logging


logger = logging.getLogger(__name__)


@implementer(ISerializeToJson)
@adapter(IGDPRCookieSettings)
class GDPRCookieSettingsSerializeToJson(ControlpanelSerializeToJson):
    def __call__(self):
        json_data = super().__call__()
        settings = json_data["data"].get("settings", "{}")
        try:
            json_data["data"]["settings"] = json.loads(settings)
        except json.decoder.JSONDecodeError:
            logger.error(f"Unable to convert value into json object: {settings}")
        return json_data
