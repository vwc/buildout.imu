from five import grok
from plone.directives import dexterity, form
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from zope import schema
from plone.app.contentlisting.interfaces import IContentListing
from imu.contacttable import MessageFactory as _

from imu.contacttable.sglcontact import ISglContact

# Interface class; used to define content-type schema.

class IContactsTable(form.Schema):   
    """
    Contacts Folder
    """
    title = schema.TextLine(
            title=_(u"Name"),
            required=True,
    )
    
    description = schema.Text(
                  title=_(u"A short summary"),
                  required=False,
    )


class ContactsTable(dexterity.Item):
    grok.implements(IContactsTable)


class ContactTableView(grok.View):
    grok.context(IContactsTable)
    grok.require('zope2.View')
    grok.name('view')    
    
    def haveSglContacts(self):
        return len(self.contained_sglcontacts()) > 0
    
    def contacts(self):
        import math
        results = IContentListing(self.contained_sglcontacts())
        count = len(results)
        rowcount = count/2.0
        rows = math.ceil(rowcount)
        matrix = []
        for i in range(int(rows)):
            row = []
            for j in range(2):
                index = 2*i + j
                if index <= int(count - 1):
                    cell = {}
                    cell['item'] = results[index]
                    row.append(cell)
            matrix.append(row)
        return matrix
    
    def contained_sglcontacts(self):
        """ Return a list of contained teasers in order to construct a item scrollable. """
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=ISglContact.__identifier__,
                          path='/'.join(context.getPhysicalPath()),
                          review_state='published',
                          sort_on='sortable_title')
        return results
