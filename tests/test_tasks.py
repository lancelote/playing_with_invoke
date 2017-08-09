from invoke import MockContext, Result

from tasks import build, building, cleaning, compile_src, hello, hi, \
    make_painting, pre_task, publishing, show_platform, task_itself
from tests.helpers import MockStdoutTestCase


class TestBuild(MockStdoutTestCase):

    def test_build_prints_correct_result(self):
        build(MockContext())
        self.assertStdout('Building!')

    def test_clean(self):
        build(MockContext(), clean=True)
        self.assertStdout('Cleaning!\nBuilding!')


class TestHi(MockStdoutTestCase):

    def test_hi_returns_correct_result_1(self):
        hi(MockContext(), name='Cassandra')
        self.assertStdout('Hi Cassandra!')

    def test_hi_return_correct_result_2(self):
        hi(MockContext(), name='Pandora')
        self.assertStdout('Hi Pandora!')


class TestShowPlatform(MockStdoutTestCase):

    def test_show_platform_on_mac(self):
        show_platform(MockContext(run=Result("Darwin")))
        self.assertInStdout('Apple')

    def test_show_platform_on_linux(self):
        show_platform(MockContext(run=Result("Linux")))
        self.assertInStdout('desktop')


class TestPreTask(MockStdoutTestCase):

    def test_prints_correct_result(self):
        pre_task(MockContext())
        self.assertStdout('Pre-task')


class TestTaskItself(MockStdoutTestCase):

    def test_print_correct_result(self):
        task_itself(MockContext())
        self.assertStdout('Task itself')


class TestCompile(MockStdoutTestCase):

    def test_no_log_given(self):
        compile_src(MockContext())
        self.assertStdout('Log value is None')

    def test_log_boolean(self):
        compile_src(MockContext(), log=True)
        self.assertStdout('Log destination is output.log\n'
                          'Log value is True')

    def test_log_value_given(self):
        compile_src(MockContext(), log='idea.log')
        self.assertStdout('Log destination is idea.log\n'
                          'Log value is idea.log')


class TestMakePainting(MockStdoutTestCase):

    def test_default_flag(self):
        make_painting(MockContext())
        self.assertStdout('Painting in colors')

    def test_invert_flag(self):
        make_painting(MockContext(), colors=False)
        self.assertStdout('Black & white painting')


class TestHello(MockStdoutTestCase):

    def test_hello_prints_correct_output(self):
        hello(MockContext())
        self.assertStdout('hello world')


class TestCleaning(MockStdoutTestCase):

    def test_cleaning_prints_correct_output(self):
        cleaning(MockContext())
        self.assertStdout('Cleaning')


class TestPublishing(MockStdoutTestCase):

    def test_publishing_pints_correct_output(self):
        publishing(MockContext())
        self.assertStdout('Publishing')


class TestBuilding(MockStdoutTestCase):

    def test_building_print_correct_output(self):
        building(MockContext())
        self.assertStdout('Building')
