import io
import sys
import unittest
from unittest.mock import patch

from invoke import MockContext, Result

from tasks import build, hi, pre_task, show_platform, task_itself


class MockStdoutTestCase(unittest.TestCase):
    def setUp(self):
        patcher = patch('sys.stdout', new=io.StringIO())
        self.addCleanup(patcher.stop)
        patcher.start()

    def assertStdout(self, expected):
        self.assertEqual(expected, sys.stdout.getvalue())

    def assertInStdout(self, expected):
        self.assertIn(expected, sys.stdout.getvalue())


class BuildTest(MockStdoutTestCase):
    def test_build_prints_correct_result(self):
        build(MockContext())
        self.assertStdout('Building!\n')

    def test_clean(self):
        build(MockContext(), clean=True)
        self.assertStdout('Cleaning!\nBuilding!\n')


class HiTest(MockStdoutTestCase):
    def test_hi_returns_correct_result_1(self):
        hi(MockContext(), name='Cassandra')
        self.assertStdout('Hi Cassandra!\n')

    def test_hi_return_correct_result_2(self):
        hi(MockContext(), name='Pandora')
        self.assertStdout('Hi Pandora!\n')


class ShowPlatformTest(MockStdoutTestCase):
    def test_show_platform_on_mac(self):
        show_platform(MockContext(run=Result("Darwin\n")))
        self.assertInStdout('Apple')

    def test_show_platform_on_linux(self):
        show_platform(MockContext(run=Result("Linux\n")))
        self.assertInStdout('desktop')


class PreTaskTest(MockStdoutTestCase):
    def test_prints_correct_result(self):
        pre_task(MockContext())
        self.assertStdout('Pre-task\n')


class TaskItselfTest(MockStdoutTestCase):
    def test_print_correct_result(self):
        task_itself(MockContext())
        self.assertStdout('Task itself\n')
