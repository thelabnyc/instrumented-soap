from setuptools import setup, find_packages, Distribution
import codecs
import os.path

# Make sure versiontag exists before going any further
Distribution().fetch_build_eggs("versiontag>=1.2.0")

from versiontag import get_version, cache_git_tag  # NOQA


packages = find_packages("src")

install_requires = [
    "Django>=2.2",
    "suds-community>=0.8.5",
    "requests>=2.9.1",
]

extras_require = {
    "development": [
        "flake8>=3.2.1",
        "tox>=2.6.0",
        "sphinx>=1.6.5",
        "sphinx-rtd-theme>=0.4.3",
    ],
}


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return codecs.open(fpath(fname), encoding="utf-8").read()


cache_git_tag()

setup(
    name="instrumented-soap",
    description="Wrapper around suds-jurko that adds improved proxy support and testing tools.",
    version=get_version(pypi=True),
    long_description=open("README.rst").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    author="Craig Weber",
    author_email="crgwbr@gmail.com",
    url="https://gitlab.com/thelabnyc/instrumented-soap",
    license="ISC",
    package_dir={"": "src"},
    packages=packages,
    install_requires=install_requires,
    extras_require=extras_require,
)
