=================
Instrumented SOAP
=================

This package is a wrapper around suds_ that adds django_statsd instrumentation and improved HTTP proxy support.

.. _suds: https://bitbucket.org/jurko/suds


Usage
=====


1. Install the `instrumented-soap` package (``pip install git+ssh://git@gitlab.com/thelabnyc/instrumented-soap.git#r1.0.0``).
2. Configure using your Django project's settings.py file. The available options and their defaults are shown below. All configuration is optional.::

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

3. Use with your SOAP API.::

    from soap import get_client

    client = get_client('http://some.dope.soap.api.com/path?WSDL', 'DOPE API LOG PREFIX')
    resp = client.service.DoStuff(42)
    print(resp)


Changelog
=========

1.0.2
------------------
- Use docker executor for tests.
- Use versiontag>=1.0.3

1.0.1
------------------
- Updated README


1.0.0
------------------
- Initial release.
