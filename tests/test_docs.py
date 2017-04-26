from invoke import MockContext

from docs import generate
from tests.helpers import MockStdoutTestCase


class GenerateDocsTest(MockStdoutTestCase):
    def test_prints_correct_result(self):
        generate(MockContext())
        self.assertStdout('Generating Docs\n')
