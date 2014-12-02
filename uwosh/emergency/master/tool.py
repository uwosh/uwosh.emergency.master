from zope.interface import implements
from zope.component import getUtility
from zope.interface import classProvides
from AccessControl import ClassSecurityInfo
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces._content import IFolderish
from plone.app.layout.navigation.root import getNavigationRoot
from Products.CMFCore.interfaces import ISiteRoot

from interfaces import IMasterEmergencyTool

from OFS.SimpleItem import SimpleItem


class MasterEmergencyTool(SimpleItem):

    implements(IMasterEmergencyTool)

    security = ClassSecurityInfo()

    _sites = ()
    _public_key = None
    _private_key = None
    
    security.declareProtected('uwosh.emergency.master: Manage master emergency settings', 'setSites')
    def setSites(self, value):
        self._sites = value
        
    security.declareProtected('uwosh.emergency.master: Manage master emergency settings', 'getSites')
    def getSites(self):
        return self._sites
