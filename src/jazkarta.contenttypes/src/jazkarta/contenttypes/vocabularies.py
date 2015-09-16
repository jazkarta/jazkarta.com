import os.path
from plone import api
from plone.app.vocabularies.catalog import KeywordsVocabulary
from plone.registry.interfaces import IRegistry
from zope.component import queryUtility
from zope.interface import alsoProvides, implementer
from zope.schema.interfaces import IContextSourceBinder, IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from jazkarta.contenttypes.interfaces import IJazSettings


def technologies(context):
    registry = queryUtility(IRegistry)
    jaz_settings = registry.forInterface(IJazSettings)
    terms = []
    for tech in jaz_settings.technologies:
        terms.append(
            SimpleVocabulary.createTerm(tech, tech.encode('utf-8'), tech))
    return SimpleVocabulary(terms)
alsoProvides(technologies, IContextSourceBinder)


class TechnologyVocabulary(KeywordsVocabulary):
    keyword_index = 'technology'
TechnologyVocabularyFactory = TechnologyVocabulary()


def industries(context):
    registry = queryUtility(IRegistry)
    jaz_settings = registry.forInterface(IJazSettings)
    terms = []
    for indst in jaz_settings.industries:
        terms.append(
            SimpleVocabulary.createTerm(indst, indst.encode('utf-8'), indst))
    return SimpleVocabulary(terms)
alsoProvides(industries, IContextSourceBinder)


class IndustryVocabulary(KeywordsVocabulary):
    keyword_index = 'industry'
IndustryVocabularyFactory = IndustryVocabulary()


def case_studies(context):
    catalog = api.portal.get_tool('portal_catalog')
    file_brains = catalog(portal_type="File")
    terms = []
    for brain in file_brains:
        token = brain.getPath()
        terms.append(SimpleTerm(
            value=brain.UID,
            token=token,
            title=brain.Title.decode('utf-8')
        ))
    return SimpleVocabulary(terms)
alsoProvides(case_studies, IContextSourceBinder)


def services(context):
    registry = queryUtility(IRegistry)
    jaz_settings = registry.forInterface(IJazSettings)
    site_path = '/'.join(
        api.portal.get_navigation_root(context).getPhysicalPath()
    )
    services_path = jaz_settings.services_location
    search_path = os.path.join(site_path, services_path.lstrip('/'))

    terms = []
    catalog = api.portal.get_tool('portal_catalog')
    # all published documents at the root level in our designated folder
    results = catalog(
        path={'query': search_path, 'depth': 1},
        portal_type="Folder",
        review_state="published"
    )
    for brain in results:
        token = brain.getPath()
        terms.append(SimpleTerm(
            value=brain.UID,
            token=token,
            title=brain.Title.decode('utf-8')
        ))
    return SimpleVocabulary(terms)
alsoProvides(services, IContextSourceBinder)


@implementer(IVocabularyFactory)
class ServiceVocabulary(object):
    keyword_index = 'services'

    def __call__(self, context, query=None):
        self.catalog = api.portal.get_tool('portal_catalog')
        if self.catalog is None:
            return SimpleVocabulary([])
        index = self.catalog._catalog.getIndex(self.keyword_index)

        def safe_encode(term):
            if isinstance(term, unicode):
                # no need to use portal encoding for transitional encoding from
                # unicode to ascii. utf-8 should be fine.
                term = term.encode('utf-8')
            return term

        brains = self.catalog(UID=tuple(index._index))
        items = [
            SimpleTerm(brain.UID, brain.getPath(), safe_encode(brain.Title))
            for brain in brains
        ]
        return SimpleVocabulary(items)
ServiceVocabularyFactory = ServiceVocabulary()


def team_members(context):
    catalog = api.portal.get_tool('portal_catalog')
    team_member_brains = catalog(portal_type='jazkarta.team_member')
    terms = []
    for brain in team_member_brains:
        token = brain.getPath()
        terms.append(SimpleTerm(
            value=brain.UID,
            token=token,
            title=brain.Title.decode('utf8')
            ))
    return SimpleVocabulary(terms)
alsoProvides(team_members, IContextSourceBinder)


class TeamVocabulary(ServiceVocabulary):
    keyword_index = 'team'
TeamVocabularyFactory = TeamVocabulary()
