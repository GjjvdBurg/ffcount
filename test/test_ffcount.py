from __future__ import print_function, division

import os
import shutil
import sys
import unittest

from ffcount import ffcount

def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)

class FFCountTestCase(unittest.TestCase):

    def setUp(self):
        self.thisdir = os.path.dirname(os.path.realpath(__file__))
        self.working_dir = os.path.join(self.thisdir, 'test_files')
        if os.path.exists(self.working_dir):
            shutil.rmtree(self.working_dir)
        os.makedirs(self.working_dir)

        d1 = os.path.join(self.working_dir, "dir1")
        d2 = os.path.join(self.working_dir, "dir2")
        os.makedirs(d1)
        os.makedirs(d2)

        touch(os.path.join(self.working_dir, "file0"))
        touch(os.path.join(self.working_dir, ".hidden"))
        touch(os.path.join(d1, "file1"))
        touch(os.path.join(d2, "file2"))


    def test_ffcount(self):
        f, d = ffcount(self.working_dir)

        self.assertEqual(f, 4)
        self.assertEqual(d, 2)


    def test_ffcount_recursive(self):
        f, d = ffcount(self.working_dir, recursive=False)

        self.assertEqual(f, 2)
        self.assertEqual(d, 2)


    def test_ffcount_hidden(self):
        # we only test this on non-windows
        if sys.platform == 'win32':
            return

        f, d = ffcount(self.working_dir, hidden=False)

        self.assertEqual(f, 3)
        self.assertEqual(d, 2)

        f, d = ffcount(self.working_dir, recursive=False, hidden=False)
        self.assertEqual(f, 1)
        self.assertEqual(d, 2)


    def tearDown(self):
        shutil.rmtree(self.working_dir, ignore_errors=False)

