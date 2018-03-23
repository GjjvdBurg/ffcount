#!/usr/bin/env python

import os
import re

from setuptools import setup, find_packages
from distutils.extension import Extension

USE_CYTHON = "auto"

if USE_CYTHON:
    try:
        from Cython.Build import cythonize
    except ImportError:
        if USE_CYTHON == "auto":
            USE_CYTHON = False
        else:
            raise

ext = '.pyx' if USE_CYTHON else '.c'
extensions = [
        Extension("ffcount.count", [
            os.path.join("src", "count" + ext),
            os.path.join("src", "c_count.c")
            ])
        ]

if USE_CYTHON:
    extensions = cythonize(extensions)

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

version = re.search("__version__ = '([^']+)'",
        open('ffcount/__init__.py').read()).group(1)

setup(
        name="ffcount",
        version=version,
        description=("Fast File Count: Recursively count files and "
            "directories very quickly"),
        long_description=read('README.rst'),
        author="G.J.J. van den Burg",
        author_email="gertjanvandenburg@gmail.com",
        url="https://github.com/GjjvdBurg/ffcount",
        license='Apache License 2.0',
        packages=find_packages(),
        ext_modules = extensions,
        classifiers=[
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3'
            ]
        )
