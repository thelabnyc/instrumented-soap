from suds.transport import Reply
from http.client import HTTPMessage
import unittest.mock as mock
import soap
import re

from .http import HttpTransport


class SoapTest(object):
    def setUp(self):
        soap.clients = {}


    def _build_transport_with_reply(self, body, status=200, pattern=None):
        headers = HTTPMessage()
        headers.add_header('Content-Type', 'text/xml; charset=utf-8')
        reply = Reply(status, headers, body)

        transport = HttpTransport()
        def surrogate(request, *args, **kwargs):
            if pattern and not re.search(pattern, request.url):
                return HttpTransport.send(transport, *args, **kwargs)
            return reply
        transport.send = mock.MagicMock()
        transport.send.side_effect = surrogate
        return transport
