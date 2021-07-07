from soap import settings
from django.test import TestCase
import soap


class SOAPTest(TestCase):
    def test_basic_soap_method_call(self):
        wsdl = "http://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL"
        client = soap.get_client(wsdl, "LOCATIONS")
        client.set_options(port="NumberConversionSoap")
        resp = client.service.NumberToWords("42")
        self.assertEqual(str(resp).strip(), "forty two")


class SOAPProxyTest(TestCase):
    def test_soap_with_proxy(self):
        """Set sandbox/settings to use"""
        if settings.PROXY_URL:
            wsdl = (
                "http://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL"
            )
            soap.get_client(wsdl, "LOCATIONS")
