# Fast File Count in Python

[![build](https://github.com/GjjvdBurg/ffcount/workflows/build/badge.svg)](https://github.com/GjjvdBurg/ffcount/actions?query=workflow%3Abuild)
[![PyPI version](https://badge.fury.io/py/ffcount.svg)](https://pypi.org/project/ffcount)
[![Python package downloads](https://pepy.tech/badge/ffcount)](https://pepy.tech/project/ffcount)

This is a Python package to quickly count the number of files and directories
in a given path. Optionally you can count recursively and include hidden files
in the total.

This package is a wrapper around ``fast-file-count`` by [Christopher Schultz
](https://github.com/ChristopherSchultz). Credit for the initial version 
belongs to Christopher Schultz, I wrote the Python wrapper, converted the 
Windows code to use builtin functionality, and packaged it up.  See the file
``src/c_count.c`` for the other contributors and see the commit history of
this package on GitHub for my exact changes.

## Installation

Installation can be done easily with pip:

```bash
$ pip install ffcount
```

## Usage

There is a command line application called ``ffcount``, which recursively 
counts files and directories:

```
$ ffcount
```

See ``ffcount -h`` for options.

The package can also be used as a Python library, using the ``ffcount`` 
function. This function returns a tuple ``(number_of_files, number_of_dirs)`` 
and it can be used as follows:

```python
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
```

Note that ``ffcount`` counts links as files, even if they point to a 
directory. In some cases, this explains the discrepancy with other ways of 
counting.

To obtain the full function documentation, simply run:

```python
>>> import ffcount
>>> help(ffcount)
```

## License

The original C code by Christopher Schultz was licensed under the Apache
License 2.0. This package is therefore licensed under this license as well.
