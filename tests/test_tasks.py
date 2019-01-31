from invoke import MockContext, Result

from tasks import show_platform


# Use MockContext
def test_show_platform_apple(capsys):
    c = MockContext(run=Result('Darwin\n'))
    show_platform(c)
    assert 'Apple' in capsys.readouterr().out


def test_show_platform_linux(capsys):
    c = MockContext(run=Result('Linux\n'))
    show_platform(c)
    assert 'Linux' in capsys.readouterr().out
