# -*- coding: utf-8 -*-
from plone import api
from zope.component import queryUtility
from zope.schema.interfaces import IVocabularyFactory


class VocabConverter(object):
    """Convert values based on a named vocabulary factory

    The converter will assume that the value to convert is the value of the
    vocabulary term, it will return the title, if available, otherwise the
    value
    """

    def __init__(self, vocab_name):
        self.vocab_name = vocab_name

    def __call__(self, value):
        """return team member name from UID"""
        portal = api.portal.get()
        factory = queryUtility(
            IVocabularyFactory, name=self.vocab_name, default=None
        )
        try:
            term = factory(portal).getTerm(value)
            return term.title or term.value
        except (AttributeError, TypeError):
            return value
        except LookupError:
            # the provided value may be private or otherwise unreachable,
            # protect by returning None.
            return None

TeamConverter = VocabConverter('jazkarta.contenttypes.team')
ServicesConverter = VocabConverter('jazkarta.contenttypes.services')
