import warnings

try:
    from django.conf import settings
except ImportError:
    pass


def overridable(name, default=None):
    try:
        return getattr(settings, name, default)
    except NameError:
        return default


#: Enables Suds request/response logging
#: Set Django ``settings.DEBUG`` to override.
DEBUG = overridable("DEBUG", False)

#: Remove the Suds file cache of pickled WSDLs upon process exit
#: Set Django ``settings.SOAP_REMOVE_CACHE_ON_EXIT`` to override.
REMOVE_CACHE_ON_EXIT = overridable("SOAP_REMOVE_CACHE_ON_EXIT", False)

#: Optional mapping of ``http(s)://`` WSDL URLs => ``file://`` URLs to locally saved
#: versions of the WSDL.
#: Set Django ``settings.SOAP_WSDL_INTERCEPTS`` to override.
WSDL_INTERCEPTS = overridable("SOAP_WSDL_INTERCEPTS", {})

#: Optional HTTP/HTTPS proxy URL
#: DEPRECATED: Use SOAP_PROXIES instead
#: Set Django ``settings.SOAP_PROXY_URL`` to override.
PROXY_URL = overridable("SOAP_PROXY_URL")
if PROXY_URL:
    warnings.warn(
        "The SOAP_PROXY_URL setting is deprecated. Migrate to the SOAP_PROXIES setting.",
        DeprecationWarning,
    )

#: Optional HTTP/HTTPS proxy URL
#: Set Django ``settings.SOAP_PROXY_URL`` to override.
#: Format:
#:
#:     SOAP_PROXIES = {
#:         "soap.my-server.com": "http://myproxy.com:3128/",
#:     }
PROXIES = overridable("SOAP_PROXIES")

#: Timeout for opening WSDLs. Should be a tuple containing (1) the TCP connect
#: timeout and (2) the response timeout.
#: Set Django ``settings.SOAP_OPEN_TIMEOUT`` to override.
OPEN_TIMEOUT = overridable("SOAP_OPEN_TIMEOUT", (3.05, 27))

#: Timeout for sending SOAP method calls. Should be a tuple containing (1) the
#: TCP connect timeout and (2) the response timeout.
#: Set Django ``settings.SOAP_SEND_TIMEOUT`` to override.
SEND_TIMEOUT = overridable("SOAP_SEND_TIMEOUT", (3.05, 10))
