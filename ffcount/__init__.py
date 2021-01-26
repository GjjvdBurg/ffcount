# -*- coding: utf-8 -*-

__version__ = "0.1.5"

# Author: Gertjan van den Burg <gertjanvandenburg@gmail.com>
#
# License: Apache License 2.0

from pathlib import Path

from typing import Tuple
from typing import Union

from .count import fast_file_count


def ffcount(
    path: Union[str, bytes, Path] = ".",
    recursive: bool = True,
    hidden: bool = True,
    quiet: bool = True,
) -> Tuple[int, int]:
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
    if isinstance(path, Path):
        path = str(path)

    if not isinstance(path, bytes):
        path = path.encode()

    return fast_file_count(path, recursive, hidden, quiet)
