import io
import sys
import unittest
from unittest.mock import patch

from invoke import MockContext, Result

from tasks import build, show_platform


class MockSysTestCase(unittest.TestCase):
    def setUp(self):
        patcher = patch('sys.stdout', new=io.StringIO())
        self.addCleanup(patcher.stop)
        patcher.start()


class BuildTest(MockSysTestCase):
    def test_build_prints_correct_result(self):
        build(MockContext())
        self.assertEqual('Building!\n', sys.stdout.getvalue())

    def test_clean(self):
        build(MockContext(), clean=True)
        self.assertEqual('Cleaning!\nBuilding!\n', sys.stdout.getvalue())


class ShowPlatformTest(MockSysTestCase):
    def test_show_platform_on_mac(self):
        c = MockContext(run=Result("Darwin\n"))
        show_platform(c)
        self.assertIn('Apple', sys.stdout.getvalue())

    def test_show_platform_on_linux(self):
        c = MockContext(run=Result("Linux\n"))
        show_platform(c)
        self.assertIn('desktop', sys.stdout.getvalue())
