#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- mode: python -*-
import sys
from setuptools import setup

if sys.hexversion < 0x02070000:
    raise RuntimeError("Python 2.7 or higher required")

# Replace all instances of `comp-neurosci-skeleton` with the name of your project
setup(
    name="comp-neurosci-crcns-lgn1",
    version="0.0.1",
    package_dir={'comp-neurosci-crcns-lgn1': 'src'},
    packages=["comp-neurosci-crcns-lgn1"],

    description="",
    long_description="",
    install_requires=[
        "numpy>=1.10",
    ],

    author="chener3",
    maintainer='chener3',
)
