import unittest
import soap


class SOAPTest(unittest.TestCase):
    def test_basic_soap_method_call(self):
        wsdl = 'http://www.webservicex.net/uszip.asmx?WSDL'
        client = soap.get_client(wsdl, 'LOCATIONS')
        client.set_options(port='USZipSoap')

        resp = client.service.GetInfoByZIP('10305')
        self.assertEquals(resp.NewDataSet.Table.CITY, 'Staten Island')
        self.assertEquals(resp.NewDataSet.Table.STATE, 'NY')
