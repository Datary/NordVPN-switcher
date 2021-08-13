import pathlib
from setuptools import setup, find_packages

DIRNAME = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'datary_nordvpn_switcher'
AUTHOR = 'Datary'
AUTHOR_EMAIL = 'engineering@datary.io'
URL = 'https://github.com/datary/nordvpn_switcher'
LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Automatic endpoint switcher for NordVPN'
LONG_DESCRIPTION = (DIRNAME / 'README.md').read_text()
LONG_DESC_TYPE = 'text/markdown'
INSTALL_REQUIRES = [
    'psutil',
    'bs4',
    'requests',
    'lxml',
    'pathlib',
    'random_user_agent'
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    package_dir={
        'datary_nordvpn_switcher': 'src'
    },
    packages=[
        'datary_nordvpn_switcher',
        'datary_nordvpn_switcher.NordVPN_options'
    ],
    include_package_data=True
)
