"""Utils for testing."""

import io
import sys
import unittest
from unittest.mock import patch


class MockStdoutTestCase(unittest.TestCase):
    def setUp(self):
        patcher = patch('sys.stdout', new=io.StringIO())
        self.addCleanup(patcher.stop)
        patcher.start()

    def assertStdout(self, expected):
        self.assertEqual(expected, sys.stdout.getvalue())

    def assertInStdout(self, expected):
        self.assertIn(expected, sys.stdout.getvalue())
