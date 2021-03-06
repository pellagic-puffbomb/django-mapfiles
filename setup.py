#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import djangomapfiles

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangomapfiles.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='dj-mapfiles',
    version=version,
    description="""A Django application for live loading and editing of shapfiles, kml files, and content from American Community Survey datasets.""",
    long_description=readme + '\n\n' + history,
    author='Erik Aker',
    author_email='eraker@gmail.com',
    url='https://github.com/pellagic-puffbomb/django-mapfiles',
    packages=[
        'djangomapfiles',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-mapfiles',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
