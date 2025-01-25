# Author: Eightman <eightman124@gmail.com>
# Copyright (c) 2020-2025 Eightman
# License: GNU GPLv3

from setuptools import setup

DESCRIPTION = "This is a test for Hoi4 Modding Tools"
NAME = "Hoi4_Modding_Tools"
AUTHOR = "Eightman"
AUTHOR_EMAIL = "eightman124@gmail.com"
LICENSE = "GNU GPLv3"
URL = ""
VERSION = "0.0.1"
DOWNLOAD_URL = ""
PYTHON_REQUIRES = ">=3.6"
INSTALL_REQUIRES = [
    "pykakasi",
    "scipy",
    "lark"
]

PACKAGES = [
    'tools',
    'pdx_tools'
]

CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Operating System :: OS Independent",
    "Natural Language :: Japanese",
    "Natural Language :: English",
    "Topic :: Utilities",
    "Topic :: Software Development :: Libraries",
    "Topic :: Hoi4 Modding"
    "Topic :: Hoi4"
    "Topic :: Modding"
]

with open('README.rst', 'r') as fp:
    readme = fp.read()
with open('CONTACT.txt', 'r') as fp:
    contacts = fp.read()
long_description = readme + '\n\n' + contacts

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=long_description,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      packages=PACKAGES,
      classifiers=CLASSIFIERS
      )