API
===

Public Interface
----------------

.. autofunction:: soap.get_client



Transports
----------

.. autoclass:: soap.http.HttpTransport
   :members:
   :undoc-members:


Django Settings
---------------

.. autodata:: soap.settings.DEBUG
.. autodata:: soap.settings.REMOVE_CACHE_ON_EXIT
.. autodata:: soap.settings.WSDL_INTERCEPTS
.. autodata:: soap.settings.PROXY_URL
.. autodata:: soap.settings.OPEN_TIMEOUT
.. autodata:: soap.settings.SEND_TIMEOUT


Logging
-------

.. autoclass:: soap.LogPlugin
   :members:
   :undoc-members:


Testing Hooks
-----------------

.. autodata:: soap.clients
.. autofunction:: soap.get_transport


Testing Utilities
-----------------

.. autoclass:: soap.tests.XMLAssertions
   :members:
   :undoc-members:
.. autoclass:: soap.tests.SoapTest
   :members:
   :undoc-members:
   :private-members:
