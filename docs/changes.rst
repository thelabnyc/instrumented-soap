Change Log
==========

1.3.0
------------------
- Add new setting ``SOAP_PROXIES``, which allows setting Soap proxies per WSDL domain. This allows, for example, using a proxy for requests to ``soap.some-api.com``, but not using a proxy for requests to ``soap.some-other-api.com``.
- Deprecate ``SOAP_PROXY_URL`` setting in favor of the new ``SOAP_PROXIES`` setting.
- Change connection pooling behavior.
    - Previously, we used ``requests.Session`` to re-use TCP connections between Soap calls.
    - This has been removed due to it causing issues with some Soap servers. A new TCP connection is now created for each request.

1.2.0
------------------
- Add ability to pass in custom plug-ins to the Suds client.

1.1.1
------------------
- Add better documentation
- Fix bug in ``soap.tests.SoapTest._build_transport_with_reply`` which broke SOAP request pass-through for domains not matching the given pattern.

1.1.0
------------------
- Add some better testing tools for consumer code.
    - New class `soap.tests.XMLAssertions` with methods: `assertNodeCount`, `assertNodeText`, `assertNodeAttributes`. Uses `lxml` if it is installed, but otherwise falls back to `elementree`.
    - Class `soap.tests.SoapTest` now inherits from `soap.tests.XMLAssertions`
    - Add optional parameter `test_request` to `soap.tests.SoapTest._build_transport_with_reply`. Pass in a function to have it called (with the request as a parameter) before the mocked reply is sent. Useful to write unit tests to make sure your SOAP requests are well-formed.

1.0.2
------------------
- Use docker executor for tests.
- Use versiontag>=1.0.3

1.0.1
------------------
- Updated README


1.0.0
------------------
- Initial release.
