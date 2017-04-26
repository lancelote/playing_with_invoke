from invoke import task


@task
def pre_task(_):
    print('Pre-task')


@task(pre_task)
def task_itself(_):
    print('Task itself')


@task
def build(_, clean=False):
    if clean:
        print('Cleaning!')
    print('Building!')


@task(help={'name': 'Name of the person to say hi to.'})
def hi(_, name):
    """Say hi to someone."""
    print('Hi %s!' % name)


@task
def show_platform(ctx):
    uname = ctx.run("uname -s").stdout.strip()
    print(platform_response(uname))


def platform_response(uname):
    if uname == 'Darwin':
        return "You paid the Apple tax!"
    elif uname == 'Linux':
        return "Year of Linux on the desktop!"
