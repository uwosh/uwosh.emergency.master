from zope.interface import Interface, Attribute
from zope import schema
from uwosh.emergency.master.config import mf as _

class IUWOshEmergencyMasterLayer(Interface):
    """Marker interface that defines a browser layer
    """

class IMasterEmergencyTool(Interface):
    """
    
    """