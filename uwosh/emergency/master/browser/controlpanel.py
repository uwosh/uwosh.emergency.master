from zope.interface import Interface, alsoProvides
from zope.component import adapts
from zope.formlib import form
from zope.interface import implements

from Products.CMFCore.interfaces import ISiteRoot
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFDefault.formlib.schema import SchemaAdapterBase

from uwosh.emergency.master.config import mf as _
from plone.app.controlpanel.form import ControlPanelForm
from zope import schema
from widgets import SitesWidget
from Products.CMFCore.utils import getToolByName

class ISitesSchema(Interface):
    """Combined schema for the adapter lookup.
    """
    
    sites = schema.List(
        title=_(u"Sites")
    )


class MasterControlPanelAdapter(SchemaAdapterBase):

    adapts(IPloneSiteRoot)
    implements(ISitesSchema)

    def __init__(self, context):
        super(MasterControlPanelAdapter, self).__init__(context)
        
        self.tool = getToolByName(context, 'portal_emergency_master')
        
    def get_sites(self):
        return self.tool.getSites()
        
    def set_sites(self, value):
        self.tool.setSites(value)
        
    sites = property(get_sites, set_sites)


class MasterControlPanel(ControlPanelForm):

    form_fields = form.FormFields(ISitesSchema)
    form_fields['sites'].custom_widget = SitesWidget
    
    label = _("Sites Settings")
    description = _("A registry of all the sites.")
        
