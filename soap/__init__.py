from django_statsd.clients import statsd
from suds.client import Client
from suds.plugin import MessagePlugin
from suds.cache import FileCache
import os.path
import pathlib
import logging

from . import settings
from .http import HttpTransport


logger = logging.getLogger(__name__)
clients = {}


# Set cache deletion preference
FileCache.remove_default_location_on_exit = settings.REMOVE_CACHE_ON_EXIT


class LogPlugin(MessagePlugin):
    def __init__(self, prefix):
        self.prefix = prefix

    def sending(self, context):
        logger.debug('%s Request: %s' % (self.prefix, context.envelope))

    def received(self, context):
        logger.debug('%s Response: %s' % (self.prefix, context.reply))


def get_transport():
    return HttpTransport()


def get_client(wsdl, log_prefix, **kwargs):
    if wsdl in settings.WSDL_INTERCEPTS:
        wsdl = settings.WSDL_INTERCEPTS[wsdl]

    if wsdl not in clients:
        plugins = []
        if settings.DEBUG:
            plugins.append( LogPlugin(log_prefix) )

        try:
            clients[wsdl] = Client(wsdl, plugins=plugins, transport=get_transport(), **kwargs)
        except Exception as e:
            statsd.incr('soap.wsdl-creation-error')
            logger.fatal('Failed to create SOAP client with WSDL at %s' % wsdl)
            raise e
    return clients[wsdl]
