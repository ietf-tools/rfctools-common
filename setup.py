#!/usr/bin/env python
# --------------------------------------------------
# Copyright The IETF Trust 2018-2019, All Rights Reserved
# --------------------------------------------------

from setuptools import setup, find_packages
from codecs import open
from os import path
import rfctools_common

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()
    long_description = long_description.replace('\r', '')

# Get the requirements from the local requirements.txt file
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as file:
    requirements = file.read().splitlines()

# Get additional items from the local MANIFEST.in file
with open(path.join(here, 'MANIFEST.in'), encoding='utf-8') as file:
    extra_files = [l.split()[1] for l in file.read().splitlines() if l]




setup(
    name='rfctools_common',

    # Versions should comply with PEP440.
    version=rfctools_common.__version__,

    description="Common routines for a set of RFC Production center tools",
    long_description=long_description,

    # The projects main homepage.
    url='https://github.com/ietf-tools/RfcEditor/tree/master/rfctools_common',

    # Author details
    author='Jim Schaad',
    author_email='ietf@augustcellars.com',

    # Choose your license
    license='Simplified BSD',

    # Classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Other Audience',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Markup :: XML',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],

    # What does your project relate to?
    keywords='RFC common',

    #
    packages=find_packages(exclude=['contrib', 'docs', 'Tests']),

    # List run-time dependencies here.
    install_requires=requirements,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',

    # List additional gorups of dependencies here.
    # extras_require=(
    #  'dev':['twine',],
    # ]

    package_data={
        'rfctools-common': ['templates/*']
    },

    zip_safe=False
)
