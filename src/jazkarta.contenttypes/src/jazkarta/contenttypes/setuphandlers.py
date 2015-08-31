# -*- coding: utf-8 -*-
import logging
from .upgrades import add_catalog_indexes

logger = logging.getLogger('jazkarta.contenttypes')


def isNotCurrentProfile(context):
    return context.readDataFile('jazkartacontenttypes_marker.txt') is None


def post_install(context):
    """Post install script"""
    if isNotCurrentProfile(context):
        return
    add_catalog_indexes(context, logger=logger)
