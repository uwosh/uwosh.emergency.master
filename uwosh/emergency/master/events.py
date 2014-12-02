from uwosh.simpleemergency.browser.controlpanel import SimpleEmergencyControlPanelAdapter
from threading import Timer
from Products.CMFCore.utils import getToolByName
from zope.component import queryMultiAdapter
import logging
logger = logging.getLogger('uwosh.emegency.master')
from urllib import urlopen, urlencode
from urlparse import urljoin
from uwosh.simpleemergency.utils import emergency_enabled
from uwosh.simpleemergency.config import text_to_test_cypher_with, SUCCESS_MESSAGE
import rsa

def update_remote_sites(event):
    qi = getToolByName(event.context, 'portal_quickinstaller')
    if not qi.isProductInstalled('uwosh.emergency.master'):
        return
    
    tool = getToolByName(event.context, 'portal_emergency_master')
    remote_sites = tool.getSites()
    adapter = SimpleEmergencyControlPanelAdapter(event.context)
    
    if len(remote_sites) > 0:

        data = {
            'last_updated' : adapter.props.getProperty('last_updated', ''),
            'emergency_message' : adapter.emergency_message,
            'enabled' : str(adapter.display_emergency),
            'show_on_all_pages' : str(adapter.show_on_all_pages)
        }
        
        # we'll urlencode it twice so we can sign it and then decode it on the other site.
        encoded_data = urlencode(data)
        data = {
            'signed_data' : rsa.sign(encoded_data, tool._private_key)
        }
        
        def do_later():
            for site, enabled in remote_sites:
                if not enabled:
                    continue
                    
                url = site.rstrip('/') + '/@@update-emergency-message'
                
                try:
                    res = urlopen(url, urlencode(data)).read()
                    if res != SUCCESS_MESSAGE:
                        raise Exception("remote site update didn't work")
                    else:
                        logging.info('Successfully updated emergency configuration on remote site %s' % site)
                except:
                    logging.warn('XXX - Updating the emergency site %s failed. Perhaps it is configured incorrectly?' % site)
                    
        
        timer = Timer(0.0, do_later) # do this in a thread so the page can return promptly
        timer.start()
