from zope.schema.interfaces import ValidationError
from zope.component import getMultiAdapter
from plone.memoize.instance import memoize
from Products.CMFCore.utils import getToolByName

from zope.app.form.interfaces import WidgetInputError
from zope.app.form.browser.interfaces import \
    ISourceQueryView, ITerms, IWidgetInputErrorView
from zope.app.form.browser.widget import SimpleInputWidget
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

from plone.app.vocabularies.interfaces import IBrowsableTerm

class SitesWidget(SimpleInputWidget):
    
    template = ViewPageTemplateFile('siteswidget.pt')

    def sites(self):
        if self.request.form.has_key('updateSelection') or self.request.form.has_key('addRow'):
            return self.getInputValue()
        else:
            return self._data

    def __call__(self):
        return self.template(self)

    @property
    @memoize
    def public_key(self):
        tool = getToolByName(self.context.context.context, 'portal_emergency_master')
        return tool._public_key
        

    def getInputValue(self):
        form = self.request.form
        value = []
        number_of_sites = int(form['numberofsites'])
        
        for i in range(0, number_of_sites):
            key_site_url = 'siteurl-%s' % i
            key_site_enabled = 'siteenabled-%s' % i
            
            if form.has_key(key_site_url):
                url = form[key_site_url]
                enabled = form.get(key_site_enabled, 'off') == 'on' and True or False
            
                if len(key_site_url) > 0:
                    
                    if form.has_key('sitedelete-%s' % i) and form['sitedelete-%s' % i] == "on":
                        pass
                    else:
                        value.append((url, enabled))
        return value

    def hasInput(self):
        form = self.request.form
        
        res = [k for k in form.keys() if 'siteurl' in k in k or 'siteenabled' in k]
        
        return len(res) > 0
    
