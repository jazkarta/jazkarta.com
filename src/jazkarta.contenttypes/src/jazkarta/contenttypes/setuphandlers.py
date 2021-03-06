# -*- coding: utf-8 -*-
import logging
from plone import api

logger = logging.getLogger('jazkarta.contenttypes')


PROFILE_ID = 'profile-jazkarta.contenttypes:default'


def isNotCurrentProfile(context):
    return context.readDataFile('jazkartacontenttypes_marker.txt') is None


def add_catalog_indexes(context, logger=None):
    """Method to add catalog indexes to the portal_catalog.
    """
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger('jazkarta.contenttypes')

    setup = api.portal.get_tool(name="portal_setup")
    setup.runImportStepFromProfile(PROFILE_ID, 'catalog')

    catalog = api.portal.get_tool('portal_catalog')
    indexes = catalog.indexes()
    # Specify the indexes you want, with ('index_name', 'index_type')
    wanted = (
        ('technology', 'KeywordIndex'),
        ('industry', 'KeywordIndex'),
        ('services', 'KeywordIndex'),
        ('team', 'KeywordIndex'),
        ('launch_date', 'DateIndex'),
    )
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info("Added %s for field %s.", meta_type, name)
    if len(indexables) > 0:
        logger.info("Indexing new indexes %s.", ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)


def post_install(context):
    """Post install script"""
    if isNotCurrentProfile(context):
        return
    add_catalog_indexes(context, logger=logger)
