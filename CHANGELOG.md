# Changes

## v2.1.2 (2024-08-31)

### Fix

- **deps**: update dependency suds-community to >=1.2.0

## v2.1.2b3 (2024-08-08)

### Fix

- **deps**: update dependency suds-community to >=1.1.2
- **deps**: update dependency requests to >=2.32.3
- **deps**: update dependency django to >=5.0.6
- **deps**: update dependency requests to v2.32.3
- **deps**: update dependency django to v4.2.13

## v2.1.1

- Fix setuptools / 2to3 issues by switching from suds-jurko to suds-community.


## v2.1.0

- Add support for Django 3.2

## v2.0.0

- Remove StatsD counters and metrics.

## v1.3.0

- Add new setting ``SOAP_PROXIES``, which allows setting Soap proxies per WSDL domain. This allows, for example, using a proxy for requests to ``soap.some-api.com``, but not using a proxy for requests to ``soap.some-other-api.com``.
- Deprecate ``SOAP_PROXY_URL`` setting in favor of the new ``SOAP_PROXIES`` setting.
- Change connection pooling behavior.
    - Previously, we used ``requests.Session`` to re-use TCP connections between Soap calls.
    - This has been removed due to it causing issues with some Soap servers. A new TCP connection is now created for each request.

## v1.2.0

- Add ability to pass in custom plug-ins to the Suds client.

## v1.1.1

- Add better documentation
- Fix bug in ``soap.tests.SoapTest._build_transport_with_reply`` which broke SOAP request pass-through for domains not matching the given pattern.

## v1.1.0

- Add some better testing tools for consumer code.
    - New class `soap.tests.XMLAssertions` with methods: `assertNodeCount`, `assertNodeText`, `assertNodeAttributes`. Uses `lxml` if it is installed, but otherwise falls back to `elementree`.
    - Class `soap.tests.SoapTest` now inherits from `soap.tests.XMLAssertions`
    - Add optional parameter `test_request` to `soap.tests.SoapTest._build_transport_with_reply`. Pass in a function to have it called (with the request as a parameter) before the mocked reply is sent. Useful to write unit tests to make sure your SOAP requests are well-formed.

## v1.0.2

- Use docker executor for tests.
- Use versiontag>=1.0.3

## v1.0.1

- Updated README


## v1.0.0

- Initial release.
