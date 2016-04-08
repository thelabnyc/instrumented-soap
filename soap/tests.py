from suds.transport import Reply
from http.client import HTTPMessage
import unittest.mock as mock
import soap
import re

from .http import HttpTransport



try:
    from lxml import etree
except ImportError:
    try:
        # Python 2.5
        import xml.etree.cElementTree as etree
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as etree
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree
                except ImportError:
                    pass



class XMLAssertions(object):
    def assertNodeCount(self, xml_str, xpath, num):
        doc = etree.fromstring(xml_str)
        nodes = doc.xpath(xpath)
        self.assertEqual(num, len(nodes))

    def assertNodeText(self, xml_str, xpath, expected):
        doc = etree.fromstring(xml_str)
        nodes = doc.xpath(xpath)
        self.assertTrue(len(nodes) > 0)
        for node in nodes:
            self.assertEqual(expected, node.text)

    def assertNodeAttributes(self, xml_str, xpath, attributes):
        doc = etree.fromstring(xml_str)
        nodes = doc.xpath(xpath)
        self.assertTrue(len(nodes) > 0)
        for node in nodes:
            for attribute, value in attributes.items():
                self.assertTrue(attribute in node.attrib)
                self.assertEqual(value, node.attrib[attribute])



class SoapTest(XMLAssertions):
    def setUp(self):
        soap.clients = {}


    def _build_transport_with_reply(self, body, status=200, pattern=None, test_request=None):
        headers = HTTPMessage()
        headers.add_header('Content-Type', 'text/xml; charset=utf-8')
        reply = Reply(status, headers, body)

        transport = HttpTransport()
        def surrogate(request, *args, **kwargs):
            if pattern and not re.search(pattern, request.url):
                return HttpTransport.send(transport, *args, **kwargs)
            if test_request:
                test_request(request)
            return reply
        transport.send = mock.MagicMock()
        transport.send.side_effect = surrogate
        return transport
