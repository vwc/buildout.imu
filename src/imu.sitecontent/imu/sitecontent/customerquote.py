from five import grok
from plone.directives import dexterity, form

from zope import schema

from z3c.form import group, field
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

from imu.sitecontent import MessageFactory as _


# Interface class; used to define content-type schema.

class ICustomerQuote(form.Schema):
    """
    A single quote by a customer.
    """
    
    title = schema.TextLine(
        title=_(u"Title"),
        description=_(u"Please enter a descriptive title for this testimonial."),
        required=True,
    )
    
    quote = schema.Text(
        title=_(u"Customer Quote"),
        description=_(u"Enter the customer testimonial here. The testimonials should roughly be of the same length."),
        required=True,
    )
    
    customer = schema.TextLine(
        title=_(u"Customer Name"),
        required=True,
    )
    
    position = schema.TextLine(
        title=_(u"Customer Position"),
        description=_(u"Please enter the position or title of the quoted person, e.g. CEO."),
        required=False,
    )
    
class CustomerQuote(dexterity.Item):
    grok.implements(ICustomerQuote)
    
    # Add your class methods and properties here

class QuoteView(grok.View):
    grok.context(ICustomerQuote)
    grok.require('zope2.View')
    grok.name('view')