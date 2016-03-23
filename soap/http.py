from django_statsd.clients import statsd
from suds.transport import Transport, Reply
import urllib.request
import logging
import requests
import io

from . import settings


logger = logging.getLogger(__name__)


class HttpTransport(Transport):
    open_timeout = settings.OPEN_TIMEOUT
    send_timeout = settings.SEND_TIMEOUT

    def __init__(self, **kwargs):
        super().__init__()
        self.session = requests.Session()

    def open(self, request):
        url = request.url
        logger.debug('Opening WSDL: %s ' % url)
        statsd.incr('soap.open')
        with statsd.timer('soap.open'):
            if url.startswith('file://'):
                content = urllib.request.urlopen(url)
            else:
                resp = self.session.get(url, proxies=self.proxies, timeout=self.open_timeout)
                resp.raise_for_status()
                content = io.BytesIO(resp.content)
        return content

    def send(self, request):
        url = request.url
        msg = request.message
        headers = request.headers
        logger.debug('Sending SOAP request: %s' % url)
        statsd.incr('soap.send')
        with statsd.timer('soap.send'):
            resp = self.session.post(url, proxies=self.proxies, timeout=self.send_timeout, data=msg, headers=headers)
        resp.raise_for_status()
        reply = Reply(requests.codes.OK, resp.headers, resp.content)
        return reply

    @property
    def proxies(self):
        proxies = {}
        if settings.PROXY_URL:
            proxies["http"] = settings.PROXY_URL
            proxies["https"] = settings.PROXY_URL
        return proxies
