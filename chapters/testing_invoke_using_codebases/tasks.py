from invoke import task


# Use MockContext
@task
def show_platform(c):
    uname = c.run('uname -s').stdout.strip()
    if uname == 'Darwin':
        print('You paid the Apple tax!')
    elif uname == 'Linux':
        print('Year of Linux on the desktop!')


# Expect Results
@task
def show_platform2(c):
    print(platform_response(c.run('uname -s')))


def platform_response(result):
    uname = result.stdout.strip()
    if uname == 'Darwin':
        return 'You paid the Apple tax!'
    elif uname == 'Linux':
        return 'Year of Linux on the desktop!'


# Avoid mocking dependency code paths altogether
@task
def show_platform3(c):
    uname = c.run('uname -s').stdout.strip()
    print(platform_response2(uname))


def platform_response2(uname):
    if uname == 'Darwin':
        return 'You paid the Apple tax!'
    elif uname == 'Linux':
        return 'Year of Linux on the desktop'
