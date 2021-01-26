#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import io

from setuptools import setup, find_packages
from distutils.extension import Extension

AUTHOR = "G.J.J. van den Burg"
DESCRIPTION = (
    "Fast File Count: Recursively count files and directories very quickly"
)
EMAIL = "gertjanvandenburg@gmail.com"
LICENSE = "Apache License 2.0"
LICENSE_TROVE = "License :: OSI Approved :: Apache Software License"
NAME = "ffcount"
REQUIRES_PYTHON = ">=3.6"
URL = "https://github.com/GjjvdBurg/ffcount"
VERSION = None
USE_CYTHON = "auto"

REQUIRED = []
EXTRAS = {}

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


def cythonize(use_cython="auto"):
    if use_cython:
        try:
            from Cython.Build import cythonize
        except ImportError:
            if use_cython == "auto":
                use_cython = False
            else:
                raise

    ext = ".pyx" if use_cython else ".c"
    extensions = [
        Extension(
            "ffcount.count",
            [
                os.path.join("src", "count" + ext),
                os.path.join("src", "c_count.c"),
            ],
        )
    ]

    if use_cython:
        extensions = cythonize(extensions)
    return extensions


setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license=LICENSE,
    packages=find_packages(exclude=["tests"]),
    package_data={"ffcount": ["py.typed"]},
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    entry_points={"console_scripts": ["ffcount = ffcount.__main__:main"]},
    ext_modules=cythonize(USE_CYTHON),
    classifiers=[
        LICENSE_TROVE,
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    zip_safe=False,
)
