import random
from zope.interface import implements

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope.formlib import form

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from imu.sitecontent.customerquote import ICustomerQuote

from imu.portlet.randomquote import RandowmQuotePortletMessageFactory as _


class IRandomQuotePortlet(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IRandomQuotePortlet)

    def __init__(self):
        pass

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return _(u"Testimonial Portlet")


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('randomquoteportlet.pt')
    
    def available(self):
        return len(self._quotes()) > 0
    
    def random_quote(self):
        quotes = self._quotes()
        rq = random.choice(quotes)
        q = {}
        rq_obj = rq.getObject()
        q['quote'] = rq_obj.quote
        q['customer'] = rq_obj.customer
        q['position'] = rq_obj.position
        return q
        
    def _quotes(self):
        """Get all customerquotes in the db and do a random choice selection"""
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        quotes = catalog(object_provides=ICustomerQuote.__identifier__,
                         review_state='published')
        return quotes

class AddForm(base.NullAddForm):
    """Portlet add form.
    """
    def create(self):
        return Assignment()

