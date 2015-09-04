from plone.indexer.decorator import indexer
from plone.supermodel import model


class IProject(model.Schema):
    model.load('models/project.xml')


@indexer(IProject)
def project_launch_date(obj, **kw):
    return obj.launch_date
