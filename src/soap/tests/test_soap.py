from soap import settings
from django.test import TestCase
import soap


class SOAPTest(TestCase):
    def test_basic_soap_method_call(self):
        wsdl = 'http://www.webservicex.net/uszip.asmx?WSDL'
        client = soap.get_client(wsdl, 'LOCATIONS')
        client.set_options(port='USZipSoap')

        resp = client.service.GetInfoByZIP('10305')
        self.assertEquals(resp.NewDataSet.Table.CITY, 'Staten Island')
        self.assertEquals(resp.NewDataSet.Table.STATE, 'NY')


class SOAPProxyTest(TestCase):
    def test_soap_with_proxy(self):
        """ Set sandbox/settings to use """
        if settings.PROXY_URL:
            wsdl = 'http://www.webservicex.net/uszip.asmx?WSDL'
            soap.get_client(wsdl, 'LOCATIONS')

    def test_private_soap_with_proxy(self):
        """ Intended for local and private use only
        Set SOAP_PROXY_URL in sandbox/settings too.
        """
        private_ip = ''
        if not private_ip:
            return
        wsdl = 'http://{}/TAXCCH/Service3.5.svc?singleWsdl'.format(private_ip)
        soap.get_client(wsdl, 'CCH')
