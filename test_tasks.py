import io
import sys
import unittest
from unittest.mock import patch

from invoke import MockContext, Result

from tasks import build, hi, show_platform


class MockStdoutTestCase(unittest.TestCase):
    def setUp(self):
        patcher = patch('sys.stdout', new=io.StringIO())
        self.addCleanup(patcher.stop)
        patcher.start()


class BuildTest(MockStdoutTestCase):
    def test_build_prints_correct_result(self):
        build(MockContext())
        self.assertEqual('Building!\n', sys.stdout.getvalue())

    def test_clean(self):
        build(MockContext(), clean=True)
        self.assertEqual('Cleaning!\nBuilding!\n', sys.stdout.getvalue())


class HiTest(MockStdoutTestCase):
    def test_hi_returns_correct_result_1(self):
        hi(MockContext(), name='Cassandra')
        self.assertEqual('Hi Cassandra!\n', sys.stdout.getvalue())

    def test_hi_return_correct_result_2(self):
        hi(MockContext(), name='Pandora')
        self.assertEqual('Hi Pandora!\n', sys.stdout.getvalue())


class ShowPlatformTest(MockStdoutTestCase):
    def test_show_platform_on_mac(self):
        c = MockContext(run=Result("Darwin\n"))
        show_platform(c)
        self.assertIn('Apple', sys.stdout.getvalue())

    def test_show_platform_on_linux(self):
        c = MockContext(run=Result("Linux\n"))
        show_platform(c)
        self.assertIn('desktop', sys.stdout.getvalue())
