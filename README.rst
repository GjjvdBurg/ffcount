Fast File Count in Python
=========================

This is a Python package to quickly count the number of files and directories
in a given path. Optionally you can count recursively and include hidden files
in the total.

This package is a wrapper around ``fast-file-count`` by `Christopher Schultz
<https://github.com/ChristopherSchultz>`_.  Credit for the initial version 
belongs to Christopher Schultz, I wrote the Python wrapper, converted the 
Windows code to use builtin functionality, and packaged it up.  See the file
``src/c_count.c`` for the other contributors and see the commit history of
this package on GitHub for my exact changes.

Installation
------------

Installation can be done easily with pip:

.. code:: bash

    pip install ffcount


Usage
-----

There is a command line application called ``ffcount`` and the package can be 
used from Python.

The Python package ``ffcount`` has only one function: ``ffcount``. This 
function returns a tuple ``(number_of_files, number_of_dirs)`` and it can be 
used as follows:

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


Note that ``ffcount`` counts links as files, even if they point to a 
directory. In some cases, this explains the discrepancy with other ways of 
counting.

Docs
----

The full documentation of the ``ffcount`` function is:

.. code:: python

    def ffcount(path='.', recursive=True, hidden=True, quiet=True):
        """Fast file count

        Count the files and directories in the given path. By default the function
        is recursive and does not print errors. This function uses the C
        implementation by Christopher Schultz.

        Parameters
        ----------
        path : str or bytes
            The path where to start counting. By default the current working
            directory will be used.

        recursive : bool
            To recurse or not to recurse. If recurse is False, only the files and
            directories in the directory given by ``path`` will be counted.

        hidden : bool
            Count hidden files and directories as well.

        quiet : bool
            Don't print errors to the screen. If True, the function will fail 
            quietly and not print any errors.

        Returns
        -------
        files_count : int
            Number of files counted.

        dir_count : int
            Number of directories counted.

        """

This can of course also be obtained by running ``help(ffcount)`` in Python.

License
-------

The original C code by Christopher Schultz was licensed under the Apache
License 2.0. This package is therefore licensed under this license as well.
