from plone import api
from plone.indexer.decorator import indexer
from Products.CMFCore.interfaces import IContentish

from .project import IProject
from .team_member import ITeamMember


@indexer(IProject)
def project_launch_date(obj, **kw):
    return obj.launch_date


@indexer(IProject)
def project_technology(obj, **kw):
    return obj.technology


@indexer(IProject)
def project_industry(obj, **kw):
    return obj.industry


@indexer(IProject)
def project_services(obj, **kw):
    return obj.services


@indexer(IProject)
def project_team(obj, **kw):
    return obj.team


@indexer(ITeamMember)
def team_member_technology(obj, **kw):
    return obj.technology


@indexer(IContentish)
def null_indexer(obj, **kw):
    return
