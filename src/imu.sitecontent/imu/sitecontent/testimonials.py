from Acquisition import aq_inner
from five import grok
from plone.directives import dexterity, form

from zope import schema

from z3c.form import group, field
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

from Products.CMFCore.utils import getToolByName

from plone.app.contentlisting.interfaces import IContentListing
from imu.sitecontent.customerquote import ICustomerQuote

from imu.sitecontent import MessageFactory as _


# Interface class; used to define content-type schema.

class ITestimonials(form.Schema):
    """
    A collection of customer testimonials.
    """
    
    form.model("models/testimonials.xml")


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Testimonials(dexterity.Container):
    grok.implements(ITestimonials)
    
    # Add your class methods and properties here


class TestimonialsView(grok.View):
    grok.context(ITestimonials)
    grok.require('zope2.View')
    grok.name('view')
    
    def testimonials(self):
        """Query the catalog for testimonials"""
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=ICustomerQuote.__identifier__,
                          review_state='published')
        contentlist = IContentListing(results)
        return contentlist
        