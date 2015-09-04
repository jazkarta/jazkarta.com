from plone import api
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from zope.component import queryUtility
from zope.interface import alsoProvides
from zope.schema.interfaces import IContextSourceBinder
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


def industries(context):
    registry = queryUtility(IRegistry)
    jaz_settings = registry.forInterface(IJazSettings)
    terms = []
    for indst in jaz_settings.industries:
        terms.append(
            SimpleVocabulary.createTerm(indst, indst.encode('utf-8'), indst))
    return SimpleVocabulary(terms)
alsoProvides(industries, IContextSourceBinder)


def services(context):
    registry = queryUtility(IRegistry)
    jaz_settings = registry.forInterface(IJazSettings)
    terms = []
    for service in jaz_settings.services:
        terms.append(
            SimpleVocabulary.createTerm(
                service, service.encode('utf-8'), service
            )
        )
    return SimpleVocabulary(terms)
alsoProvides(services, IContextSourceBinder)


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
