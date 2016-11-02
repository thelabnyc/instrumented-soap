Getting Started
===============

Installation
------------

Install the instrumented-soap package.

.. code:: bash

    pip install instrumented-soap


Configure using your Django project's settings.py file. The available options and their defaults are shown below. All configuration is optional. See the :data:`soap.settings <soap.settings.DEBUG>` documentation for more information about the available configuration options.

.. code:: python

    # Enables Suds request/response logging
    DEBUG = True

    # Remove the Suds file cache of pickled WSDLs upon process exit
    SOAP_REMOVE_CACHE_ON_EXIT = False

    # Optional mapping of http(s):// WSDL URLs => file:// URLs to locally saved versions of the WSDL
    SOAP_WSDL_INTERCEPTS = {}

    # Optional HTTP/HTTPS proxy URL
    SOAP_PROXY_URL = None

    # Timeouts for opening WSDLs and sending method calls. Should be a
    # tuple containing (1) the TCP connect timeout and (2) the response
    # timeout.
    SOAP_OPEN_TIMEOUT = (3.05, 27)
    SOAP_SEND_TIMEOUT = (3.05, 10)


Usage
-----

Use with your SOAP API.

.. code:: python

    >>> from soap import get_client
    >>> client = get_client('http://some.dope.soap.api.com/path?WSDL', 'DOPE API LOG PREFIX')
    >>> resp = client.service.DoStuff(42)
    >>> print(resp)
