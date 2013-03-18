from five import grok
from plone.directives import dexterity, form
from zope import schema

from plone.namedfile.field import NamedImage
from plone.namedfile.field import NamedBlobImage

from plone.namedfile.interfaces import IImageScaleTraversable

from imu.partnertable import MessageFactory as _


# Interface class; used to define content-type schema.

class ISglPartner(form.Schema, IImageScaleTraversable):
    """
    single partner
    """
    title = schema.TextLine(
        title=_(u"Nachname"),
        required=True,
    )

    aTitle = schema.TextLine(
        title=_(u"Vorname"),
        required=True,
    )

    bTitle = schema.TextLine(
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
    picture = NamedBlobImage(
        title=_(u"Portrait"),
        required=False,
    )
    form.widget(main="plone.app.z3cform.wysiwyg.widget.WysiwygFieldWidget")
    main = schema.Text(
        title=_(u"Main Content"),
        required=False,
    )
    email = schema.TextLine(
        title=_(u"Email"),
        required=False,
    )


class SglPartner(dexterity.Item):
    grok.implements(ISglPartner)


class SglPartnerView(grok.View):
    grok.context(ISglPartner)
    grok.require('zope2.View')
    grok.name('view')
