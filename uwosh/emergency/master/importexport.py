
se_default_profile = 'profile-uwosh.simpleemergency:default'
from Products.CMFCore.utils import getToolByName
from uwosh.simpleemergency.utils import disable_emergency
import rsa

def install(context):
    
    if not context.readDataFile('uwosh.emergency.master.txt'):
        return
    
    # install simple emergency propertiestool
    # to store settings
    site = context.getSite()
    
    qi = getToolByName(site, 'portal_quickinstaller')
    if qi.isProductInstalled('uwosh.simpleemergency') or qi.isProductInstalled('uwosh.emergency.client'):
        raise Exception('You can not install uwosh.simpleemrgency or uwosh.emergency.client on the same site as the master.')
    
    portal_setup = getToolByName(site, 'portal_setup')
    portal_setup.runImportStepFromProfile(se_default_profile, 'propertiestool')
    portal_setup.runImportStepFromProfile(se_default_profile, 'cssregistry')
    disable_emergency(site) # disable by default
    
    # install public/private key
    tool = getToolByName(site, 'portal_emergency_master')
    if not tool._public_key or not tool._private_key:
        tool._public_key, tool._private_key = rsa.gen_pubpriv_keys(512)
        
        
        
def uninstall(context):
    
    if not context.readDataFile('uwosh.emergency.master-uninstall.txt'):
        return
    
    site = context.getSite()
    
    cp = getToolByName(site, 'portal_controlpanel')
    cp.unregisterApplication("uwosh.emergency.master")