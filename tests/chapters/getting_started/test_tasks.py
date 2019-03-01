import pytest
from invoke import MockContext

from chapters.getting_started.tasks import build, build2, hi


def test_build(capsys):
    build(MockContext())
    assert 'building' in capsys.readouterr().out


def test_build2_clean(capsys):
    build2(MockContext(), clean=True)
    out = capsys.readouterr().out
    assert 'cleaning' in out
    assert 'building' in out


def test_build2_not_clean(capsys):
    build2(MockContext())
    out = capsys.readouterr().out
    assert 'cleaning' not in out
    assert 'building' in out


@pytest.mark.parametrize('name', ['Pavel', 'John', 'Jane'])
def test_hi(capsys, name):
    hi(MockContext(), name=name)
    assert name in capsys.readouterr().out
