from plone.supermodel import model


class IClient(model.Schema):
    model.load('models/client.xml')
