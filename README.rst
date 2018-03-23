Fast File Count in Python
=========================

This is a Python package to quickly count the number of files and directories 
in a given path. Optionally you can count recursively and include hidden files 
in the total.

This package is a wrapper around ``fast-file-count`` by `Christopher Schultz 
<https://github.com/ChristopherSchultz>`_.  All credit belongs to Christopher 
Schultz, I only wrote the Python wrapper and packaged it up. See the file 
``src/c_count.c`` for the other contributors and see the commit history of 
this package on GitHub for my exact changes.

Installation
------------

Installation can be done easily with pip:

.. code:: bash

    pip install ffcount


Usage
-----

The package ``ffcount`` has only one function: ``ffcount``. It can be used as 
follows:

.. code:: python

    >>> from ffcount import ffcount

    # count everything under the current path
    >>> ffcount()
    (521013, 43012)

    # count without hidden files
    >>> ffcount(hidden=False)
    (234012, 12082)

    # use a different path
    >>> ffcount('/tmp')
    (81, 10)

License
-------

The original C code by Christopher Schultz was licensed under the Apache 
License 2.0. This package is therefore licensed under this license as well.
