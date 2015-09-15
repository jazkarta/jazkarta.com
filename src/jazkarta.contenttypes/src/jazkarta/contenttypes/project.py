from plone import api
from plone.indexer.decorator import indexer
from plone.supermodel import model


class IProject(model.Schema):
    model.load('models/project.xml')
