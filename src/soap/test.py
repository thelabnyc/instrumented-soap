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
    """
    Unit test mixin to add XPath assertions on XML data.
    """

    def assertNodeCount(self, xml_str, xpath, num):
        """
        Assert that N number of the given node exist.

        :param xml_str: XML to test
        :param xpath: XPath query to run
        :param num: Number of nodes that the XPath query should return
        """
        doc = etree.fromstring(xml_str)
        nodes = doc.xpath(xpath)
        self.assertEqual(num, len(nodes))

    def assertNodeText(self, xml_str, xpath, expected):
        """
        Assert that each node returned by the XPath equals the given text.

        :param xml_str: XML to test
        :param xpath: XPath query to run
        :param expected: Expected string content
        """
        doc = etree.fromstring(xml_str)
        nodes = doc.xpath(xpath)
        self.assertTrue(len(nodes) > 0)
        for node in nodes:
            self.assertEqual(expected, node.text)

    def assertNodeAttributes(self, xml_str, xpath, attributes):
        """
        Assert that each node returned by the XPath has each of the given attributes and attribute values.

        :param xml_str: XML to test
        :param xpath: XPath query to run
        :param expected: Dictionary of attribute names and their expected values
        """
        doc = etree.fromstring(xml_str)
        nodes = doc.xpath(xpath)
        self.assertTrue(len(nodes) > 0)
        for node in nodes:
            for attribute, value in attributes.items():
                self.assertTrue(attribute in node.attrib)
                self.assertEqual(value, node.attrib[attribute])


class SoapTest(XMLAssertions):
    """
    Subclass of :class:`soap.tests.XMLAssertions <soap.tests.XMLAssertions>` that adds behavior useful for
    mocking and testing a SOAP API at the XML level.
    """

    def setUp(self):
        """Test Setup. Clears the :attr:`soap.clients <soap.clients>` cache."""
        soap.clients = {}

    def _build_transport_with_reply(
        self, body, status=200, pattern=None, test_request=None
    ):
        """
        Build a fake :class:`soap.http.HttpTransport <soap.http.HttpTransport>` that, when called, will
        reply with the given XML body and status code.

        :param body: XML response data as bytes.
        :param status: HTTP status code to return.
        :param pattern: Optional. Regexp pattern to match against the request URL. Useful if your
                        test communicates with multiple SOAP APIs that need different mock responses.
        :param test_request: Optional. Function to call with a request object, before returning
                             the response. Can use this to run assertions on the SOAP request XML.
        :return: :class:`soap.http.HttpTransport <soap.http.HttpTransport>` object
        :rtype: soap.http.HttpTransport
        """
        headers = HTTPMessage()
        headers.add_header("Content-Type", "text/xml; charset=utf-8")
        reply = Reply(status, headers, body)

        transport = HttpTransport()

        def surrogate(request, *args, **kwargs):
            if pattern and not re.search(pattern, request.url):
                return HttpTransport.send(transport, request, *args, **kwargs)
            if test_request:
                test_request(request)
            return reply

        transport.send = mock.MagicMock()
        transport.send.side_effect = surrogate
        return transport
