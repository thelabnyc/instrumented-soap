try:
    from django.conf import settings
except ImportError:
    pass

def overridable(name, default=None):
    try:
        return getattr(settings, name, default)
    except NameError:
        return default

# Enables Suds request/response logging
DEBUG = overridable('DEBUG', False)

# Remove the Suds file cache of pickled WSDLs upon process exit
REMOVE_CACHE_ON_EXIT = overridable('SOAP_REMOVE_CACHE_ON_EXIT', False)

# Optional mapping of http(s):// WSDL URLs => file:// URLs to locally saved versions of the WSDL
WSDL_INTERCEPTS = overridable('SOAP_WSDL_INTERCEPTS', {})

# Optional HTTP/HTTPS proxy URL
PROXY_URL = overridable('SOAP_PROXY_URL')

# Timeouts for opening WSDLs and sending method calls. Should be a
# tuple containing (1) the TCP connect timeout and (2) the response
# timeout.
OPEN_TIMEOUT = overridable('SOAP_OPEN_TIMEOUT', (3.05, 27))
SEND_TIMEOUT = overridable('SOAP_SEND_TIMEOUT', (3.05, 10))
