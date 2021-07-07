from suds.client import Client
from suds.plugin import MessagePlugin
from suds.cache import FileCache
from .http import HttpTransport
from . import settings
import logging


logger = logging.getLogger(__name__)


#: Cache of :class:`suds.client.Client <suds.client.Client>` objects
#: When unit-testing SOAP APIs it's probably wise to reset this to an empty
#: dictionary in-between tests.
clients = {}


# Set cache deletion preference
FileCache.remove_default_location_on_exit = settings.REMOVE_CACHE_ON_EXIT


class LogPlugin(MessagePlugin):
    """Suds plugin used in DEBUG mode. Logs all incoming and outgoing XML data at the DEBUG level."""

    def __init__(self, prefix):
        self.prefix = prefix

    def sending(self, context):
        """Called when sending a SOAP request"""
        logger.debug("%s Request: %s" % (self.prefix, context.envelope))

    def received(self, context):
        """Called when receiving a SOAP response"""
        logger.debug("%s Response: %s" % (self.prefix, context.reply))


def get_transport():
    """
    Build a new :class:`soap.http.HttpTransport <soap.http.HttpTransport>` object. Unit tests can patch this
    function to return a custom transport object for the client to use. This can be useful when trying to mock
    an API rather than actually call it during a test.

    :return: :class:`soap.http.HttpTransport <soap.http.HttpTransport>` object
    :rtype: soap.http.HttpTransport
    """
    return HttpTransport()


def get_client(wsdl, log_prefix, plugins=[], **kwargs):
    """
    Get a SOAP Client object for the given WSDL. Client objects are cached in :attr:`soap.clients <soap.clients>`
    and keyed by the WSDL URL.

    :param wsdl: String URL of a SOAP WSDL
    :param log_prefix: String prefix to prepend to log lines (when logging XML traffic in DEBUG mode)
    :param plugins: List of additional plugins :class:`suds.plugin.Plugin <suds.plugin.Plugin>` to pass on to the
        :class:`suds.client.Client <suds.client.Client>` object.
    :param kwargs: Optional keyword arguments to pass on to the :class:`suds.client.Client <suds.client.Client>` object
    :return: :class:`suds.client.Client <suds.client.Client>` object
    :rtype: suds.client.Client
    """
    if wsdl in settings.WSDL_INTERCEPTS:
        wsdl = settings.WSDL_INTERCEPTS[wsdl]

    if wsdl not in clients:
        if settings.DEBUG:
            plugins.append(LogPlugin(log_prefix))

        try:
            clients[wsdl] = Client(
                wsdl, plugins=plugins, transport=get_transport(), **kwargs
            )
        except Exception as e:
            logger.fatal("Failed to create SOAP client with WSDL at %s" % wsdl)
            raise e
    return clients[wsdl]
