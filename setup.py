#!/usr/bin/env python

import os
import re

from setuptools import setup, find_packages
from distutils.extension import Extension

USE_CYTHON = "auto"

if USE_CYTHON:
    try:
        from Cython.Distutils import build_ext
    except ImportError:
        if USE_CYTHON == "auto":
            USE_CYTHON = False
        else:
            raise

cmdclass = {}
ext_modules = []

if USE_CYTHON:
    ext_modules += [
            Extension("ffcount.count", [
                os.path.join("src", "count.pyx"),
                os.path.join("src", "c_count.c")
                ])
            ]
    cmdclass.update({"build_ext": build_ext})
else:
    ext_modules += [
            Extension("ffcount.count", [
                os.path.join("src", "count.c"),
                os.path.join("src", "c_count.c")
                ])
            ]

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
        license='Apache License 2.0',
        packages=find_packages(),
        cmdclass=cmdclass,
        ext_modules=ext_modules,
        classifiers=[
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3'
            ]
        )

