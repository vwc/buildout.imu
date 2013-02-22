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

from imu.contacttable import MessageFactory as _


# Interface class; used to define content-type schema.

class ISglContact(form.Schema):
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
#            constraint=isValidEmail,
            required=False,
    )
    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/contacttype.xml to define the content type
    # and add directives here as necessary.


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class SglContact(dexterity.Item):
    grok.implements(ISglContact)
    
    # Add your class methods and properties here

# View class
# The view will automatically use a similarly named template in
# contacttype_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SglContactView(grok.View):
    grok.context(ISglContact)
    grok.require('zope2.View')
    grok.name('view')
