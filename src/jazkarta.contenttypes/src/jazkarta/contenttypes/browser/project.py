from plone import api
from Products.Five import BrowserView
from zope.cachedescriptors.property import Lazy as lazy_property


class ProjectView(BrowserView):

    @lazy_property
    def services(self):
        catalog = api.portal.get_tool('portal_catalog')
        uids = self.context.services
        results = catalog(UID=tuple(uids))
        return results

    @lazy_property
    def case_study(self):
        catalog = api.portal.get_tool('portal_catalog')
        uid = self.context.case_study
        try:
            return catalog(UID=uid)[0]
        except IndexError:
            return None
