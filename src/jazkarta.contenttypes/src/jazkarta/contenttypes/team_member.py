from plone.indexer.decorator import indexer
from plone.supermodel import model


class ITeamMember(model.Schema):
    model.load('models/team_member.xml')
