from plone.indexer.decorator import indexer
from plone.supermodel import model


class IProject(model.Schema):
    model.load('models/project.xml')


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
    return [team_member.UID for team_member in obj.team]
