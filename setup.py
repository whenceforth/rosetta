from distutils.core import setup

DISTNAME = 'DSpy'
LICENSE = 'BSD'
MAINTAINER = "The DsPy Development Team"
EMAIL = ""
URL = "https://github.com/columbia-applied-data-science/dspy"
DESCRIPTION = ""

setup(
    name=DISTNAME,
    version='0.1.0dev',
    packages=['dspy',],
    license=LICENSE,
    url=URL,
    maintainer_email=EMAIL,
    maintainer=MAINTAINER,
    description=DESCRIPTION,
    long_description=open('README.md').read()
)