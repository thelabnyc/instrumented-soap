from suds.transport import Transport, Reply
from . import settings
import urllib.request
import urllib.parse
import logging
import requests
import io


logger = logging.getLogger(__name__)


class HttpTransport(Transport):
    """
    Custom HTTPTransport to replace :class:`suds.transport.http.HttpTransport <suds.transport.http.HttpTransport>`.

    The default :class:`suds.transport.http.HttpTransport <suds.transport.http.HttpTransport>` class has issues with
    sending SOAP traffic through HTTP proxies like Squid. This Transport fixes the HTTP Proxy issues by using
    python-requests instead of urllib2.
    """

    #: Timeout for opening a WSDL file. Tuple (CONNECT_TIMEOUT, READ_TIMEOUT)
    open_timeout = settings.OPEN_TIMEOUT

    #: Timeout for sending a SOAP call. Tuple (CONNECT_TIMEOUT, READ_TIMEOUT)
    send_timeout = settings.SEND_TIMEOUT

    def open(self, request):
        """
        Open a SOAP WSDL

        :param request: :class:`suds.transport.Request <suds.transport.Request>` object
        :return: WSDL Content as a file-like object
        :rtype: io.BytesIO
        """
        url = request.url
        logger.debug("Opening WSDL: %s " % url)
        if url.startswith("file://"):
            content = urllib.request.urlopen(url)
        else:
            resp = requests.get(
                url, proxies=self.proxies(url), timeout=self.open_timeout
            )
            resp.raise_for_status()
            content = io.BytesIO(resp.content)
        return content

    def send(self, request):
        """
        Send a SOAP method call

        :param request: :class:`suds.transport.Request <suds.transport.Request>` object
        :return: :class:`suds.transport.Reply <suds.transport.Reply>` object
        :rtype: suds.transport.Reply
        """
        url = request.url
        msg = request.message
        headers = request.headers
        logger.debug("Sending SOAP request: %s" % url)
        resp = requests.post(
            url,
            proxies=self.proxies(url),
            timeout=self.send_timeout,
            data=msg,
            headers=headers,
        )
        resp.raise_for_status()
        reply = Reply(requests.codes.OK, resp.headers, resp.content)
        return reply

    def proxies(self, url):
        """
        Get the transport proxy configuration

        :param url: string
        :return: Proxy configuration dictionary
        :rtype: Dictionary
        """
        netloc = urllib.parse.urlparse(url).netloc
        proxies = {}
        if settings.PROXIES and settings.PROXIES.get(netloc):
            proxies["http"] = settings.PROXIES[netloc]
            proxies["https"] = settings.PROXIES[netloc]
        elif settings.PROXY_URL:
            proxies["http"] = settings.PROXY_URL
            proxies["https"] = settings.PROXY_URL
        return proxies
