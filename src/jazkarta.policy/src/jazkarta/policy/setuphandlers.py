# -*- coding: utf-8 -*-
import logging
from Products.CMFCore.utils import getToolByName
from Products.PortalTransforms.Transform import make_config_persistent

logger = logging.getLogger('jazkarta.policy.setuphandlers')


def isNotCurrentProfile(context):
    return context.readDataFile('jazkartapolicy_marker.txt') is None


def post_install(context):
    """Post install script"""
    if isNotCurrentProfile(context):
        return

    # Setup portal_transforms
    logger.info('Updating portal_transform safe_html settings')

    tid = 'safe_html'

    pt = getToolByName(context, 'portal_transforms')
    if tid not in pt.objectIds():
        return

    trans = pt[tid]

    tconfig = trans._config
    tconfig['nasty_tags'] = {'applet': '1'}
    tconfig['remove_javascript'] = 1
    tconfig['stripped_attributes'] = ['lang', 'valign', 'halign', 'border',
                                      'frame', 'rules', 'cellspacing',
                                      'cellpadding', 'bgcolor']
    tconfig['stripped_combinations'] = {}
    tconfig['style_whitelist'] = ['text-align', 'list-style-type', 'float',
                                  'width', 'height', 'padding-left',
                                  'padding-right']
    valid_tags = tconfig['valid_tags']
    valid_tags['embed'] = 0
    valid_tags['iframe'] = 1
    valid_tags['object'] = 1
    valid_tags['script'] = 1

    make_config_persistent(tconfig)
    trans._p_changed = True
    trans.reload()
