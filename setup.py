#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import jmauricio
version = jmauricio.__version__

setup(
    name='jmauricio',
    version=version,
    author="Jose Mauricio Oliveira e Silva",
    author_email='grandemau@gmail.com',
    packages=[
        'jmauricio',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.4',
    ],
    zip_safe=False,
    scripts=['jmauricio/manage.py'],
)
