from five import grok
from plone.directives import dexterity, form
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from zope import schema
from zope.component import getUtility
from zope.component import getMultiAdapter
from plone.app.imaging.scale import ImageScale
from plone.app.imaging.scaling import ImageScaling
from plone.namedfile.field import NamedImage
from Products.CMFPlone.utils import safe_unicode

from z3c.form import group, field
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

from imu.partnertable import MessageFactory as _


# Interface class; used to define content-type schema.

class ISglPartner(form.Schema):
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
    
    form.widget(main="plone.app.z3cform.wysiwyg.widget.WysiwygFieldWidget")
    main = schema.Text(
           title=_(u"Main Content"),
           required=False,
    )
    
    email = schema.TextLine(
            title=_(u"Email"),
            required=False,
    )
    
    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/partnertype.xml to define the content type
    # and add directives here as necessary.


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class SglPartner(dexterity.Item):
    grok.implements(ISglPartner)
    
    # Add your class methods and properties here

# View class
# The view will automatically use a similarly named template in
# partnertype_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SglPartnerView(grok.View):
    grok.context(ISglPartner)
    grok.require('zope2.View')
    grok.name('view')
