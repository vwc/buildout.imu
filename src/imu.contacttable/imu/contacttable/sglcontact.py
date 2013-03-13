from five import grok
from plone.directives import dexterity, form
from zope import schema
from plone.namedfile.field import NamedImage

from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

from plone.namedfile.interfaces import IImageScaleTraversable

from imu.contacttable import MessageFactory as _


# Interface class; used to define content-type schema.

class ISglContact(form.Schema, IImageScaleTraversable):
    """
    single contact
    """
    title = schema.TextLine(
        title=_(u"Nachname"),
        required=True,
    )

    vTitle = schema.TextLine(
        title=_(u"Vorname"),
        required=True,
    )

    tTitle = schema.TextLine(
        title=_(u"Titel"),
        required=False,
    )

    description = schema.Text(
        title=_(u"Abschluss / Position"),
        required=False,
    )
    image = NamedImage(
        title=_(u"Picture"),
        description=_(u"Please upload an image"),
        required=False,
    )
    form.widget(vita="plone.app.z3cform.wysiwyg.widget.WysiwygFieldWidget")
    vita = schema.Text(
        title=_(u"Main Content"),
        required=False,
    )

    phone = schema.TextLine(
        title=_(u"Tel."),
        required=False,
    )

    fax = schema.TextLine(
        title=_(u"Fax"),
        required=False,
    )

    mobile = schema.TextLine(
        title=_(u"Mobile"),
        required=False,
    )
    email = schema.TextLine(
        title=_(u"E-Mail"),
        required=False,
    )


class SglContact(dexterity.Item):
    grok.implements(ISglContact)


class SglContactView(grok.View):
    grok.context(ISglContact)
    grok.require('zope2.View')
    grok.name('view')
