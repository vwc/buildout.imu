import random
from Acquisition import aq_inner
from five import grok
from plone.directives import dexterity, form

from zope import schema

from z3c.form import group, field
from plone.app.textfield import RichText
from z3c.relationfield.schema import RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from Products.CMFCore.utils import getToolByName

from plone.app.contentlisting.interfaces import IContentListing
from plone.app.folder.folder import IATUnifiedFolder
from plone.app.blob.interfaces import IATBlobImage
from imu.sitecontent.customerquote import ICustomerQuote

from imu.sitecontent import MessageFactory as _


# Interface class; used to define content-type schema.

class ILandingPage(form.Schema):
    """
    Description of the Example Type
    """
    
    introduction = RichText(
        title=_(u"Introductional Text"),
        description=_(u"Enter an introductional text that will be displayed at the bottom of the frontpage."),
        required=True,
    )
    imagefolder = RelationChoice(
        title=_(u"Gallery Folder"),
        description=_(u"Please select a folder that will be used as a source for the gallery."),
        source=ObjPathSourceBinder(object_provides=IATUnifiedFolder.__identifier__),
        required=True,
    )


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class LandingPage(dexterity.Item):
    grok.implements(ILandingPage)
    
    # Add your class methods and properties here


class LandingPageView(grok.View):
    grok.context(ILandingPage)
    grok.require('zope2.View')
    grok.name('view')
    
    def images(self):
        """Use the selected source folder to provide images for the teaser gallery"""
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        gallery_source = context.imagefolder.to_path
        results = catalog(object_provides=IATBlobImage.__identifier__,
                          path=dict(query=gallery_source, depth=1),
                          sort_on='getObjPositionInParent')
        return results
    
    def testimonial(self):
        """Return a random testimonial for the front page box"""
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=ICustomerQuote.__identifier__,
                          review_state='published')
        selected = random.choice(results)
        result = {}
        result['quote'] = selected.getObject().quote
        result['name'] = selected.getObject().customer
        result['position'] = selected.getObject().position
        return result
        
