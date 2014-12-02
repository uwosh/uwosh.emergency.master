Emergency Master
================
This package is a Plone product designed to distribute emergency notifications
to other client sites that have uwosh.emergency.client installed. This product
works the same way in which uwosh.simpleemergency does, but also distributes the
emergency notifications to other sites.


Security
--------

Upon installation of the product, the site creates a public and private key. 
In order for the client sites to accept the master site's push notifications
of the emergency messages, they'll need to register the master site's public
key. Detailed information on how to do this can be found on the 
uwosh.emergency.client package page.

After the product is installed, you can add client sites by going to the 
`Emergency Notification Sites` control panel page and you can edit your
emergency message by going to the `Emergency configuration` control 
panel page.



Compatibility
-------------

Plone 3 and 4


Uninstall
---------

To uninstall deactivate the product in the plone control panel and also run the import step `Master Emergency Notification Uninstall Profile` in the zmi -> portal_setup -> Import tab.