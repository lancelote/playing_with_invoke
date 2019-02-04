from invoke import MockContext, Result

from tasks import platform_response, platform_response2, show_platform


# Use MockContext
def test_show_platform_apple(capsys):
    c = MockContext(run=Result('Darwin\n'))
    show_platform(c)
    assert 'Apple' in capsys.readouterr().out


def test_show_platform_linux(capsys):
    c = MockContext(run=Result('Linux\n'))
    show_platform(c)
    assert 'Linux' in capsys.readouterr().out


# Expect Results
def test_platform_response_on_mac():
    assert 'Apple' in platform_response(Result('Darwin\n'))


def test_platform_response_on_linux():
    assert 'Linux' in platform_response(Result('Linux\n'))


# Avoid mocking dependency code paths altogether
def test_platform_response_on_mac2():
    assert 'Apple' in platform_response2('Darwin\n')


def test_platform_response_on_linux2():
    assert 'Linux' in platform_response2('Linux\n')
