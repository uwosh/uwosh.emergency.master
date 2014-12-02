# handle push notifications

from uwosh.simpleemergency.browser.controlpanel import SimpleEmergencyControlPanelAdapter
from uwosh.simpleemergency.events import SimpleEmergencyModifiedEvent
from uwosh.simpleemergency.config import SUCCESS_MESSAGE
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Acquisition import aq_inner
import rsa
from zope.event import notify
        
            
class PublicKey(BrowserView):
    
    def __call__(self):
        tool = getToolByName(aq_inner(self.context), 'portal_emergency_master')
        return tool._public_key
