try:
    import _thread
except ImportError:
    _thread = None
import importlib
import os
import os.path
import shutil
import sys
from test import support
import unittest
import warnings

with warnings.catch_warnings():
    warnings.simplefilter('ignore', PendingDeprecationWarning)
    import imp


def requires_load_dynamic(meth):
    """Decorator to skip a test if not running under CPython or lacking
    imp.load_dynamic()."""
    meth = support.cpython_only(meth)
    return unittest.skipIf(not hasattr(imp, 'load_dynamic'),
                           'imp.load_dynamic() required')(meth)


@unittest.skipIf(_thread is None, '_thread module is required')
class LockTests(unittest.TestCase):
    """Very basic test of import lock functions."""

    def verify_lock_state(self, expected):
        self.assertEqual(imp.lock_held(), expected,
                         "expected imp.lock_held() to be %r" % expected)

    def testLock(self):
        LOOPS = 50

        # The import lock may already be held, e.g. if the test suite is run
        # via "import test.autotest".
        lock_held_at_start = imp.lock_held()
        self.verify_lock_state(lock_held_at_start)

        for i in range(LOOPS):
            imp.acquire_lock()
            self.verify_lock_state(True)

        for i in range(LOOPS):
            imp.release_lock()

        # The original state should be restored now.
        self.verify_lock_state(lock_held_at_start)

        if not lock_held_at_start:
            try:
                imp.release_lock()
            except RuntimeError:
                pass
            else:
                self.fail("release_lock() without lock should raise "
                          "RuntimeError")


class ImportTests(unittest.TestCase):
    def setUp(self):
        mod = importlib.import_module('test.encoded_modules')
        self.test_strings = mod.test_strings
        self.test_path = mod.__path__

    def test_import_encoded_module(self):
        for modname, encoding, teststr in self.test_strings:
            mod = importlib.import_module('test.encoded_modules.'
                                          'module_' + modname)
            self.assertEqual(teststr, mod.test)

    def test_find_module_encoding(self):
        for mod, encoding, _ in self.test_strings:
            with imp.find_module('module_' + mod, self.test_path)[0] as fd:
                self.assertEqual(fd.encoding, encoding)

        path = [os.path.dirname(__file__)]
        with self.assertRaises(SyntaxError):
            imp.find_module('badsyntax_pep3120', path)

    def test_issue1267(self):
        for mod, encoding, _ in self.test_strings:
            fp, filename, info = imp.find_module('module_' + mod,
                                                 self.test_path)
            with fp:
                self.assertNotEqual(fp, None)
                self.assertEqual(fp.encoding, encoding)
                self.assertEqual(fp.tell(), 0)
                self.assertEqual(fp.readline(), '# test %s encoding\n'
                                 % encoding)

        fp, filename, info = imp.find_module("tokenize")
        with fp:
            self.assertNotEqual(fp, None)
            self.assertEqual(fp.encoding, "utf-8")
            self.assertEqual(fp.tell(), 0)
            self.assertEqual(fp.readline(),
                             '"""Tokenization help for Python programs.\n')

    def test_issue3594(
