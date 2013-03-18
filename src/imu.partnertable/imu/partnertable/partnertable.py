import math
from five import grok
from plone.directives import dexterity, form
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from zope import schema
from plone.app.contentlisting.interfaces import IContentListing
from imu.partnertable import MessageFactory as _

from imu.partnertable.sglpartner import ISglPartner


class IPartnerTable(form.Schema):
    """
    Partner Folder
    """
    title = schema.TextLine(
        title=_(u"Name"),
        required=True,
    )
    description = schema.Text(
        title=_(u"A short summary"),
        required=False,
    )


class PartnerTable(dexterity.Item):
    grok.implements(IPartnerTable)


class PartnerTableView(grok.View):
    grok.context(IPartnerTable)
    grok.require('zope2.View')
    grok.name('view')

    def haveSglPartner(self):
        return len(self.contained_sglpartner()) > 0

    def partner(self):
        results = IContentListing(self.contained_sglpartner())
        count = len(results)
        rowcount = count / 2.0
        rows = math.ceil(rowcount)
        matrix = []
        for i in range(int(rows)):
            row = []
            for j in range(2):
                index = 2 * i + j
                if index <= int(count - 1):
                    cell = {}
                    cell['item'] = results[index]
                    row.append(cell)
            matrix.append(row)
        return matrix

    def contained_sglpartner(self):
        """ Return a list of contained teasers in order to construct a
            item scrollable.
        """
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=ISglPartner.__identifier__,
                          path='/'.join(context.getPhysicalPath()),
                          review_state='published',
                          sort_on='sortable_title')
        return results
