from collective.volto.gdprcookie import _
from collective.volto.gdprcookie.config import DEFAULT_SETTINGS
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema import Bool
from zope.schema import SourceText

import json


class ICollectiveVoltoGdprcookieLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IGDPRCookieSettings(Interface):
    banner_enabled = Bool(
        title=_("banner_enabled_label", default="Banner enabled"),
        description=_(
            "banner_enabled_help",
            default="If selected, the cookie banner will be prompt to the users.",
        ),
        default=True,
    )
    show_icon = Bool(
        title=_("show_icon_label", default="Show banner preferences icon"),
        description=_(
            "show_icon_help",
            default="If selected, the preferences icon will be shown.",
        ),
        default=True,
    )

    technical_cookies_only = Bool(
        title=_("technical_cookies_only_label", default="Technical cookies only"),
        description=_(
            "technical_cookies_only_help",
            default="Select this to enable only the technical cookies part of the banner.",
        ),
        default=False,
    )

    settings = SourceText(
        title=_("settings_label", default="Cookie banner configuration"),
        description="",
        required=True,
        default=json.dumps(DEFAULT_SETTINGS),
    )
