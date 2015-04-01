from plone.app.registry.browser import controlpanel

from jaz.contenttypes.interfaces import IJazSettings


class JazSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IJazSettings
    label = u'Jaz contenttypes settings'
    description = u""""""

    def updateFields(self):
        super(JazSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(JazSettingsEditForm, self).updateWidgets()


class JazSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = JazSettingsEditForm
