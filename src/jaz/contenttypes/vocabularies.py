from plone.registry.interfaces import IRegistry
from zope.component import queryUtility
from zope.interface import alsoProvides
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary

from jaz.contenttypes.interfaces import IJazSettings




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
