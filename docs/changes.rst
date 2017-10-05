Change Log
==========

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
