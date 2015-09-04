from zope.interface import Interface
from zope import schema


class IJazSettings(Interface):

    technologies = schema.List(
        title=u'Technologies',
        description=u'Enter possible areas of technological expertise',
        value_type=schema.TextLine()
        )

    industries = schema.List(
        title=u'Industries',
        description=u'Enter possible areas of client insutry',
        value_type=schema.TextLine()
        )

    services = schema.List(
        title=u'Services',
        description=u'Enter names of services provided by Jazkarta',
        value_type=schema.TextLine()
        )
