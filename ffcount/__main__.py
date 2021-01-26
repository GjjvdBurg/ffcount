#!/usr/bin/env python

"""Command line application for ffcount

Author: G.J.J. van den Burg
License: See LICENSE file.

"""

import argparse
import sys

from pathlib import Path

from . import ffcount
from .__version__ import __version__


def parse_args():
    parser = argparse.ArgumentParser(
        description="Fast file and directory count"
    )
    parser.add_argument(
        "path",
        help="Root path to start the counting",
        default=["."],
        nargs="*",
    )
    parser.add_argument(
        "-d",
        "--dirs-only",
        action="store_true",
        help="Ignore paths that aren't directories",
    )
    parser.add_argument(
        "-n",
        "--no-recursive",
        action="store_true",
        help="Don't count recursively",
    )
    parser.add_argument(
        "-i",
        "--no-hidden",
        action="store_true",
        help="Don't include hidden files",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose mode (shows errors)",
    )
    parser.add_argument(
        "-V",
        "--version",
        help="Show version and exit",
        action="version",
        version=__version__,
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if len(args.path) == 1:
        files, dirs = ffcount(
            args.path[0],
            recursive=not args.no_recursive,
            hidden=not args.no_hidden,
            quiet=not args.verbose,
        )
        print(f"{files} {dirs}")
    else:
        for path in args.path:
            if args.dirs_only:
                path = Path(path)
                if not path.is_dir():
                    continue
            files, dirs = ffcount(
                path,
                recursive=not args.no_recursive,
                hidden=not args.no_hidden,
                quiet=not args.verbose,
            )
            print(f"{path}: {files} {dirs}")


if __name__ == "__main__":
    sys.exit(main())
