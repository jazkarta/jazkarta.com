from plone.indexer.decorator import indexer
from plone.supermodel import model


class IClient(model.Schema):
    model.load('models/client.xml')


@indexer(IClient)
def client_launch_date(obj, **kw):
    return obj.launch_date
